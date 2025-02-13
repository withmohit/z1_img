import React from "react";
import axios from "axios";

const TwitterAuth = () => {
  const handlePostImages = async () => {
    try {
      const response = await axios.post("https://z1-imgback.onrender.com/post");
      alert("Images posted to X successfully!");
    } catch (error) {
      alert("Failed to post images");
      console.error(error);
    }
  };

  return <button onClick={handlePostImages}>Post to X</button>;
};

export default TwitterAuth;
