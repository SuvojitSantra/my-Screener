# How to Publish Your Stock Screener for Free
You can host this website online for free in less than 2 minutes. Here are the two best methods.

## Method 1: Netlify Drop (Easiest & Fastest)
**Best for:** Quick testing without using Git/Command Line.

1.  **Locate your folder**: Open your file explorer and find the folder `c:\stock market screener`.
2.  **Go to Netlify**: Open [app.netlify.com/drop](https://app.netlify.com/drop) in your browser.
3.  **Drag and Drop**: Drag the entire `stock market screener` folder onto the box that says "Drag and drop your site folder here".
4.  **Wait**: Netlify will upload and deploy your site in a few seconds.
5.  **Done**: You will get a random URL (e.g., `peaceful-galaxy-123.netlify.app`). You can share this link with anyone!

## Method 2: GitHub Pages (Professional)
**Best for:** Long-term projects where you want to update code easily.

1.  **Create a Repository**: Go to GitHub.com and create a new public repository (e.g., `my-stock-screener`).
2.  **Upload Files**:
    -   If you know Git: `git init`, `git add .`, `git commit -m "Initial commit"`, `git push`.
    -   **Web Upload**: Go to your new repository page, click "Add file" > "Upload files", and drag all files from your folder (`index.html`, etc.) there. Commit changes.
3.  **Enable Pages**:
    -   Go to **Settings** tab in your repository.
    -   Click **Pages** on the left sidebar.
    -   Under **Branch**, select `main` (or `master`) and click **Save**.
4.  **Done**: Your site will be live at `https://yourusername.github.io/my-stock-screener/`.

## Important Note
Since this is a client-side application (HTML/JS only), it works perfectly on these static hosting platforms. The "Run Screener" feature uses the mock data we added, so it doesn't need a backend server.
