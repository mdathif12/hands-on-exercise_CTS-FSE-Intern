import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://api.digitalnurture.com",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization =
      "Bearer mock-token-12345";
    return config;
  },
  (error) => Promise.reject(error)
);

apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    return Promise.reject({
      message:
        error.response?.data?.message ||
        "Request Failed",
      statusCode:
        error.response?.status || 500,
    });
  }
);

export default apiClient;