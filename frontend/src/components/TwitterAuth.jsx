// import React, { useState } from "react";

// const TwitterPost = () => {
//   const [file, setFile] = useState(null);
//   const [tweetText, setTweetText] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [message, setMessage] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handlePost = async () => {
//     if (!file) {
//       alert("Please select an image!");
//       return;
//     }

//     setLoading(true);
//     setMessage("");

//     const formData = new FormData();
//     formData.append("file", file);
//     formData.append("tweet_text", tweetText);

//     try {
//       const response = await fetch("http://localhost:8000/post", {
//         method: "POST",
//         body: formData,
//       });

//       const data = await response.json();

//       if (!response.ok) throw new Error(data.detail || "Tweet failed!");

//       setMessage(`✅ Tweet posted successfully! View it here: 
//         👉 [Tweet Link](https://twitter.com/user/status/${data.tweet_id})`);
//     } catch (error) {
//       console.error("Error posting to Twitter:", error);
//       setMessage("❌ Failed to post tweet. Please try again.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div style={{ maxWidth: "400px", margin: "auto", textAlign: "center" }}>
//       <h2>Post Image to Twitter</h2>
//       <input type="file" onChange={handleFileChange} />
//       <input
//         type="text"
//         placeholder="Tweet text..."
//         value={tweetText}
//         onChange={(e) => setTweetText(e.target.value)}
//       />
//       <button onClick={handlePost} disabled={loading}>
//         {loading ? "Posting..." : "Post to Twitter"}
//       </button>
//       {message && <p>{message}</p>}
//     </div>
//   );
// };

// export default TwitterPost;

import React from "react";

const TwitterAuth = () => {
  const handleLogin = async () => {
    const response = await fetch("http://localhost:8000/auth/login");
    const data = await response.json();
    window.location.href = data.login_url; // Redirect to Twitter login
  };

  return (
    <div>
      <h2>Login with Twitter</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default TwitterAuth;