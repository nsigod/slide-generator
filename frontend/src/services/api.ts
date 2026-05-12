const API_BASE_URL = 'http://localhost:8001'

export interface GenerateRequest {
  text: string;
  output_format: 'revealjs' | 'markdown';
}

export interface GenerateResponse {
  success: boolean;
  content: string;
  message?: string;
}

export interface ParseLinkRequest {
  share_url: string;
}

export interface ParseLinkResponse {
  success: boolean;
  content: string;
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

  async generateFromLink(share_url: string, output_format: 'revealjs' | 'markdown'): Promise<GenerateResponse> {
    const response = await fetch(`${API_BASE_URL}/api/generate-from-link`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ share_url, output_format }),
    });
    return response.json();
  },
};
