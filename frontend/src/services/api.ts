// 根据环境变量或默认值确定 API 地址
const API_BASE_URL = import.meta.env.VITE_API_URL || '';

export interface GenerateRequest {
  text: string;
  format: 'revealjs' | 'markdown';
}

export interface GenerateResponse {
  success: boolean;
  content: string;
  format?: string;
  message?: string;
}

export interface ParseLinkRequest {
  url: string;
}

export interface ParseLinkResponse {
  success: boolean;
  title?: string;
  content?: string;
  message?: string;
}

export const apiService = {
  async generateSlides(request: GenerateRequest): Promise<GenerateResponse> {
    const response = await fetch(`${API_BASE_URL}/api/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });
    return response.json();
  },

  async parseLink(request: ParseLinkRequest): Promise<ParseLinkResponse> {
    const response = await fetch(`${API_BASE_URL}/api/parse-link`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });
    return response.json();
  },
};
