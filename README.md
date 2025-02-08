<h1>Selenium WebDriver Automation Scripts</h1>

<h2>Overview</h2>
<p>
  This repository contains automation scripts developed using Selenium WebDriver and Python.
  Here, I have used Page Object Model to automate the Homapage, login and cart page.
  
</p>

<hr />

<h2>Features and Topics Covered</h2>

<h3>1. Basic Browser Operations</h3>
<ul>
  <li><strong>Open Browser:</strong> Launch a web browser using WebDriver.</li>
  <li><strong>Open URL:</strong> Navigate to a specific URL.</li>
  <li><strong>Close/Quit Browser:</strong> Properly terminate the browser session.</li>
  <li><strong>Thread Sleep:</strong> Pause script execution using <code>Thread.sleep</code> for demonstration purposes.</li>
</ul>

<h3>2. Headless Browser Testing</h3>
<ul>
  <li>Execute browser operations in headless mode to improve speed and efficiency.</li>
  <li>Retrieve the page title in a headless browser environment.</li>
</ul>

<h3>3. TestNG Annotations</h3>
<p>Implement various TestNG annotations for structured and maintainable test scripts:</p>
<ul>
  <li><strong>Before Annotations:</strong> <code>@BeforeSuite</code>, <code>@BeforeTest</code>, <code>@BeforeClass</code>, <code>@BeforeMethod</code></li>
  <li><strong>Test Annotation:</strong> <code>@Test</code></li>
  <li><strong>After Annotations:</strong> <code>@AfterMethod</code>, <code>@AfterClass</code>, <code>@AfterTest</code>, <code>@AfterSuite</code></li>
</ul>

<h3>4. Web Element Locators</h3>
<p>Utilized different locators to identify and interact with web elements:</p>
<ul>
  <li><strong>ID</strong></li>
  <li><strong>Name</strong></li>
  <li><strong>Link Text</strong></li>
  <li><strong>Partial Link Text</strong></li>
  <li><strong>Tag Name</strong></li>
  <li><strong>Class Name</strong></li>
  <li><strong>CSS Selector</strong></li>
  <li><strong>XPath</strong></li>
</ul>

<h3>5. Assertions</h3>
<ul>
  <li><strong>Hard Assertions:</strong> Verify conditions and immediately stop execution if the assertion fails.</li>
  <li><strong>Soft Assertions:</strong> Collect all assertion results and continue script execution.</li>
</ul>

<h3>6. Browser Navigation</h3>
<ul>
  <li>Navigate forward.</li>
  <li>Navigate backward.</li>
  <li>Refresh the current page.</li>
</ul>



<h2>Prerequisites</h2>
<p>Ensure the following software and tools are installed before running the scripts:</p>
<ul>
  <li><strong>Pycharm (JDK)</strong></li>
  <li><strong>Pytest</strong></li>
  <li><strong>Selenium WebDriver</strong></li>
  <li><strong>TestNG Framework</strong></li>
</ul>

<hr />

<h2>Dependencies</h2>
<p>Add the following dependencies to your <code>pom.xml</code> file:</p>
<pre>
<code>
&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.seleniumhq.selenium&lt;/groupId&gt;
        &lt;artifactId&gt;selenium-java&lt;/artifactId&gt;
        &lt;version&gt;4.x.x&lt;/version&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.testng&lt;/groupId&gt;
        &lt;artifactId&gt;testng&lt;/artifactId&gt;
        &lt;version&gt;7.x.x&lt;/version&gt;
        &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;
</code>
</pre>

<hr />

<h2>How to Use</h2>
<ol>
  <li>Clone this repository.</li>
  <li>Open the project in your preferred IDE.</li>
  <li>Configure the <code>pom.xml</code> file with the required dependencies.</li>
  <li>Run the test scripts using TestNG.</li>
</ol>

