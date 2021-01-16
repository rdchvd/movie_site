# movie_site
Simple web application on flask: movie site.

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3</li>
  <li>pip3 to install dependencies</li>
  <li>PostgreSQL</li>
  </ul>

<h3>Installing packages</h3>
<h4>Mac OS:</h4>
<ol>
 <li>Run <code>virtualenv env</code> to make virtual environment </li>
 <li>Activate it by <code>source env/bin/activate</code></li>
  <i>Then u'll see: <code>(name_of_new_virtual_env_dir)path:\to\ur\dir</code></i>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>
 <h4>Windows:</h4>
<ol>
 <li>Run <code>python3 -m venv venv</code> to make virtual environment </li>
 <li>Activate it by <code>venv\Scripts\activate.bat</code></li>
 <li>Run <code>pip3 install -r requirements.txt</code></li>
 </ol>
 

<h3>Setting up the local DB</h3>
<ol>
<li>CD into the app directory</li>
<li>Run <code>python3 manage.py db init</code></li>
<li><code>python3 manage.py migrate</code></li>
<li><code>python3 manage.py upgrade</code></li>
</ol>

<h3>Running the app</h3>
<p>Run using <code>python3 main.py</code></p>


