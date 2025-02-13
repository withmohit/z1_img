import React from "react";
import ImageUpload from "../components/ImageUpload";
import TwitterAuth from "../components/TwitterAuth";

const Home = () => {
  return (
    <div className="container">
      <h1>Image Resizer & X Poster</h1>
      <ImageUpload />
      <TwitterAuth />
    </div>
  );
};

export default Home;
