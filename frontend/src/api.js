import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const translateText = async (text, targetLang) => {
  const response = await axios.post(`${API_URL}/translate`, { text, targetLang });
  return response.data;
};

export const searchWord = async (word) => {
  const response = await axios.get(`${API_URL}/dictionary/${word}`);
  return response.data;
};
