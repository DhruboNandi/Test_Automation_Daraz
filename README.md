<h1>TestProject: Selenium Python Automation Framework</h1>

<h2>Overview</h2>
<p>
  This project is a Selenium-based Python automation framework designed for testing web applications. 
  It is built using the Page Object Model (POM) design pattern and incorporates cross-browser testing, TestNG Annotations,
  explicit waits, locators, and the pytest testing framework.
</p>

<hr />

<h2>Technologies Used</h2>
<ul>
  <li><strong>Programming Language:</strong> Python</li>
  <li><strong>Framework:</strong> Selenium, Pytest</li>
  <li><strong>Design Pattern:</strong> Page Object Model (POM)</li>
  <li><strong>Features:</strong>Locators, Waits, Cross-Browser Testing</li>
</ul>

<hr />

<h2>Features</h2>
<ul>
  <li><strong>Page Object Model:</strong> Implements reusable and maintainable page classes for web elements.</li>
  <li><strong>Cross-Browser Testing:</strong> Tests can run on multiple browsers like Edge, Firefox, etc.</li>
  <li><strong>Wait Mechanism:</strong> Uses explicit waits to ensure stable test execution.</li>
  <li><strong>Locators:</strong> Leverages ID, XPath, CSS Selector, and other locators for identifying elements.</li>
  <li><strong>Pytest:</strong> Provides fixtures, assertions, and parametrization for structured testing.</li>
</ul>

<hr />

<h2>Setup Instructions</h2>
<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/your-repo/TestProject.git</code></pre>
  <li>Navigate to the project directory:</li>
  <pre><code>cd TestProject</code></pre>
  <li>Install dependencies:</li>
  <pre><code>pip install -r requirements.txt</code></pre>
  <li>Run the tests:</li>
  <pre><code>pytest</code></pre>
</ol>

<hr />

<h2>How to Use</h2>
<p>
  Configure the <code>config.ini</code> file in the <code>Configuration</code> folder for setting up URLs, browser type, etc.
</p>
<p>
  Implement your test cases in the <code>test</code> folder using the page classes from the <code>pages</code> directory.
</p>

<hr />

<h2>Dependencies</h2>
<pre>
<code>
selenium==4.x.x
pytest==7.x.x
pytest-html==3.x.x
</code>
</pre>

<hr />



