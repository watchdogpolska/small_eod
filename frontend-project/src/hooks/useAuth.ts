import { TokenResponse } from '@/services/definitions';
import { UsersService } from '@/services/users';
import SmallEodClient from '@/utils/sdk';

export function useAuth() {
  const ACCESS_TOKEN = 'accessToken';
  const REFRESH_TOKEN = 'refreshToken';
  const EXPIRES = 'expires';

  function initSDK(accessToken) {
    const clientBearer = SmallEodClient.ApiClient.instance.authentications.Bearer;
    clientBearer.apiKey = accessToken ? `Bearer ${accessToken}` : undefined;
  }

  function setTokens(response: TokenResponse): void {
    localStorage.setItem(ACCESS_TOKEN, response.accessToken);
    localStorage.setItem(REFRESH_TOKEN, response.refreshToken);
    localStorage.setItem(EXPIRES, String(response.expiresIn));
    initSDK(response.accessToken);
  }

  function refreshToken(): void {
    if (isLoggedIn())
      UsersService.refresh({ refreshToken: localStorage.getItem(REFRESH_TOKEN) })
        .then(response => setTokens(response))
        .catch(() => logout());
  }

  function expires(): number {
    return isLoggedIn() ? Number(localStorage.getItem(EXPIRES)) : 10000;
  }

  function isLoggedIn(): boolean {
    return Boolean(localStorage.getItem(ACCESS_TOKEN) && localStorage.getItem(REFRESH_TOKEN));
  }

  function logout(): void {
    localStorage.removeItem(ACCESS_TOKEN);
    localStorage.removeItem(REFRESH_TOKEN);
    initSDK(undefined);
    window.location.href = '/login/sign-in';
  }

  // Init SDK
  if (isLoggedIn()) {
    const accessToken = localStorage.getItem(ACCESS_TOKEN);
    initSDK(accessToken);
  }

  return {
    isLoggedIn,
    setTokens,
    refreshToken,
    expires,
    logout,
  };
}
