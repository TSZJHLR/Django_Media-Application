<h1 align="center">Django Media Management Application</h1>

<p align="center">
  A simple web application to upload, view, delete, and download media files.
  <br>
  Built with <strong>Django</strong> and uses basic <strong>JavaScript</strong> for an interactive user interface.
</p>

<hr>

<h2>📖 Features</h2>
<ul>
  <li>Upload media files (images, videos, or audio).</li>
  <li>View uploaded files embedded directly in the web interface.</li>
  <li>Download uploaded files directly.</li>
  <li>Delete media files, removing them from the server.</li>
  <li>File validations:
    <ul>
      <li>Only files with extensions <code>.mp3</code>, <code>.mp4</code>, <code>.jpeg</code>, <code>.png</code>, <code>.gif</code> are allowed.</li>
      <li>File size must be between 100KB and 10MB.</li>
    </ul>
  </li>
  <li>Simple notification system (success/error messages) for user feedback.</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>
<p>Below is an overview of the directory structure:</p>

<pre>
<code>.
├── app/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── media/uploads/
├── management/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
</code>
</pre>

<hr>

<h2>📜 Requirements</h2>
<p>The following dependencies are required to run the project:</p>
<ul>
  <li>Django (v4.x)</li>
  <li>Python (v3.10)</li>
</ul>

<hr>

<h2>🔧 Installation & Setup</h2>

<ol>

  <li><strong>Create a virtual environment (optional but recommended):</strong>
    <pre><code>conda create -n media-app python=3.10 -y
conda activate media-app</code></pre>
  </li>

  <li><strong>Install dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Apply migrations:</strong>
    <pre><code>python manage.py migrate</code></pre>
  </li>

  <li><strong>Run the development server:</strong>
    <pre><code>python manage.py runserver</code></pre>
  </li>

  <li><strong>Visit the application in your browser:</strong>
    <pre><code>http://127.0.0.1:8000/</code></pre>
  </li>
</ol>
