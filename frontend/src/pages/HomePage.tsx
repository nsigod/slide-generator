import { useState } from 'react'
import { apiService } from '../services/api'

function HomePage() {
  const [inputText, setInputText] = useState('')
  const [shareUrl, setShareUrl] = useState('')
  const [outputFormat, setOutputFormat] = useState<'revealjs' | 'markdown'>('revealjs')
  const [generatedContent, setGeneratedContent] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleGenerateFromText = async () => {
    if (!inputText.trim()) {
      setError('请输入文字内容')
      return
    }

    setLoading(true)
    setError('')

    try {
      const response = await apiService.generateSlides({
        text: inputText,
        output_format: outputFormat,
      })
      if (response.success) {
        setGeneratedContent(response.content)
      } else {
        setError(response.message || '生成失败')
      }
    } catch (err) {
      setError('请求失败：' + (err instanceof Error ? err.message : '未知错误'))
    } finally {
      setLoading(false)
    }
  }

  const handleParseLink = async () => {
    if (!shareUrl.trim()) {
      setError('请输入DeepSeek分享链接')
      return
    }

    setLoading(true)
    setError('')

    try {
      const response = await apiService.parseLink({
        share_url: shareUrl,
      })
      if (response.success) {
        setInputText(response.content)
      } else {
        setError(response.message || '解析失败')
      }
    } catch (err) {
      setError('请求失败：' + (err instanceof Error ? err.message : '未知错误'))
    } finally {
      setLoading(false)
    }
  }

  const handleGenerateFromLink = async () => {
    if (!shareUrl.trim()) {
      setError('请输入DeepSeek分享链接')
      return
    }

    setLoading(true)
    setError('')

    try {
      const response = await apiService.generateFromLink(shareUrl, outputFormat)
      if (response.success) {
        setGeneratedContent(response.content)
      } else {
        setError(response.message || '生成失败')
      }
    } catch (err) {
      setError('请求失败：' + (err instanceof Error ? err.message : '未知错误'))
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = () => {
    if (!generatedContent) return

    const blob = new Blob([generatedContent], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = outputFormat === 'revealjs' ? 'slides.html' : 'slides.md'
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const handlePreview = () => {
    if (!generatedContent) return

    if (outputFormat === 'revealjs') {
      const blob = new Blob([generatedContent], { type: 'text/html' })
      const url = URL.createObjectURL(blob)
      window.open(url, '_blank')
    } else {
      // Markdown预览
      const previewWindow = window.open('', '_blank')
      if (previewWindow) {
        previewWindow.document.write(`
          <!DOCTYPE html>
          <html>
          <head>
            <title>Markdown Preview</title>
            <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
            <style>
              body { max-width: 800px; margin: 40px auto; padding: 20px; font-family: system-ui; line-height: 1.6; }
              pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
              code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; }
            </style>
          </head>
          <body>
            <div id="content"></div>
            <script>
              document.getElementById('content').innerHTML = marked.parse(\`${generatedContent.replace(/`/g, '\\`')}\`);
            </script>
          </body>
          </html>
        `)
      }
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-semibold text-gray-900">文字转幻灯片</h1>
          <p className="mt-1 text-sm text-gray-600">粘贴文字或DeepSeek分享链接，生成Reveal.js幻灯片或Markdown文件</p>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Left Column - Input */}
          <div className="space-y-6">
            {/* Text Input */}
            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-lg font-medium text-gray-900 mb-4">文字输入</h2>
              <textarea
                className="w-full h-48 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="粘贴要转换为幻灯片的文字..."
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
              />
              <div className="mt-4 flex items-center space-x-4">
                <label className="inline-flex items-center">
                  <input
                    type="radio"
                    className="form-radio"
                    name="format"
                    value="revealjs"
                    checked={outputFormat === 'revealjs'}
                    onChange={() => setOutputFormat('revealjs')}
                  />
                  <span className="ml-2">Reveal.js幻灯片</span>
                </label>
                <label className="inline-flex items-center">
                  <input
                    type="radio"
                    className="form-radio"
                    name="format"
                    value="markdown"
                    checked={outputFormat === 'markdown'}
                    onChange={() => setOutputFormat('markdown')}
                  />
                  <span className="ml-2">Markdown文件</span>
                </label>
              </div>
              <button
                className="mt-4 w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50"
                onClick={handleGenerateFromText}
                disabled={loading}
              >
                {loading ? '生成中...' : '生成幻灯片'}
              </button>
            </div>

            {/* Link Input */}
            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-lg font-medium text-gray-900 mb-4">DeepSeek分享链接</h2>
              <input
                type="text"
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="粘贴DeepSeek分享链接..."
                value={shareUrl}
                onChange={(e) => setShareUrl(e.target.value)}
              />
              <div className="mt-4 flex space-x-2">
                <button
                  className="flex-1 bg-gray-600 text-white py-2 px-4 rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 disabled:opacity-50"
                  onClick={handleParseLink}
                  disabled={loading}
                >
                  解析链接
                </button>
                <button
                  className="flex-1 bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 disabled:opacity-50"
                  onClick={handleGenerateFromLink}
                  disabled={loading}
                >
                  直接生成
                </button>
              </div>
            </div>
          </div>

          {/* Right Column - Output */}
          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-medium text-gray-900">输出预览</h2>
              {generatedContent && (
                <div className="space-x-2">
                  <button
                    className="px-3 py-1 text-sm bg-gray-200 text-gray-700 rounded hover:bg-gray-300"
                    onClick={handlePreview}
                  >
                    预览
                  </button>
                  <button
                    className="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
                    onClick={handleDownload}
                  >
                    下载
                  </button>
                </div>
              )}
            </div>

            {error && (
              <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-md">
                {error}
              </div>
            )}

            {generatedContent ? (
              <div className="border border-gray-200 rounded-md p-4 h-96 overflow-auto">
                <pre className="whitespace-pre-wrap text-sm text-gray-700">{generatedContent}</pre>
              </div>
            ) : (
              <div className="border-2 border-dashed border-gray-300 rounded-md p-12 text-center h-96 flex items-center justify-center">
                <p className="text-gray-500">生成的内容将在这里显示</p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  )
}

export default HomePage
