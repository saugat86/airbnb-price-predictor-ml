import axios from "axios";

export const makeModelsPost = async (postData) => {
  
  // Fix CORS policy error: Response to preflight request 
  // doesn't pass access control check: Redirect is not allowed 
  // for a preflight request.
 const customHeader = {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      "Chace-ControlType": ['no-chace', 'no-store', 'must-revalidate'] ,
      'Pragma': 'no-cache',
      'Expires': 0
    },
  };
  console.log(postData); // Used for debugging
  
 

  const res = await axios.post('http://127.0.0.1:5000/models', postData, customHeader);  

  console.log(res.data); // Used for debugging

  const data = await res.data;

  return data;
};

export const getStats = async () => {
  const res = await axios("http://127.0.0.1:5000/stats");
  const data = await res.data;

  return data;
};