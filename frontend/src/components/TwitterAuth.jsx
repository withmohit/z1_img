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
