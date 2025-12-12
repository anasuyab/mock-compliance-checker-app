// src/setupProxy.js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  // This tells the React development server to forward all
  // requests starting with /api to the target URL.
  app.use(
    '/api',
    createProxyMiddleware({
      // We target the request to Vercel's internal serverless function 
      // endpoint, which Vercel dev sets up.
      target: 'http://localhost:3000', 
      changeOrigin: true,
      
      // Crucial: Rewrite the path if the serverless functions were in a subfolder.
      // Since yours are in /api, no path rewrite is needed.
    })
  );
};