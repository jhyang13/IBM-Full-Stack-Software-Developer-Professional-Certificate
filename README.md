# IBM-Full-Stack-Software-Developer-Professional-Certificate

## Introduction to HTML, CSS, & JavaScript
### By learning the fundamentals of HTML5, CSS, and JavaScript you will be able to combine them to:  
- create the basic structure of a website  
- create format and layout for web applications 
- enhance your website and create rich, interactive applications 
- increase user interactivity and enhance user experience 
- give your website a real wow factor

### Single Page Portfolio Website 

**File Path:** `Introduction_to_HTML_CSS_JavaScript`/`singlepagewebsite`/`index.html`

**Preview HTML:** https://htmlpreview.github.io/

**Input**: https://github.com/jhyang13/IBM-Full-Stack-Software-Developer-Professional-Certificate/blob/main/Introduction_to_HTML_CSS_JavaScript/singlepagewebsite/index.html

![image](https://github.com/user-attachments/assets/b2163f64-949a-4a63-9678-3aafd2ea2a10)

## Developing Front-End Apps with React
### What you'll learn
- Develop interactive user interfaces (UIs) and web applications using JavaScript technologies including React, JSX, and ES6
- Build dynamic front-end applications quickly and easily with reusable React components
- Employ various React concepts and features, including props, states, hooks, forms, and Redux
- Demonstrate your React skills by building several front-end applications such as a shopping cart

**URL of the Final Project:** https://jhyang13.github.io/e-plantShopping/

![image](https://github.com/user-attachments/assets/3e23923e-40f4-42d0-8744-dfb9966ebd3b)

## Developing Back-End Apps with Node.js and Express
### What you'll learn
- Create server-side applications using the Node.js JavaScript run time
- Extend your Node.js applications with third-party packages and frameworks, including Express
- Use npm to manage Node.js packages in your Node.js application
- Develop asynchronous callback functions and promises to complete asynchronous operations

## Django Application Development with SQL and Databases
### What you'll learn
- Explain what a database is and create an entity relationship data model for a relational database
- Compose SQL queries to insert, select, update, and delete data in a database
- Use Django ORM to build object-oriented databases
- Integrate Bootstrap into your Django template and build interactive web pages

## Application Development using Microservices and Serverless
### What you'll learn
- Summarize the fundamentals of Microservices, their advantages, and contrast with monolithic architectures
- Create REST API endpoints and invoke them using cURL and Postman; Use SwaggerUI to document and test APIs
- Create, and deploy microservices using Docker containers and serverless technologies like IBM Code Engine
- Practice hands-on with labs and projects using a no-charge cloud-based environment

** URLs of Final Project: Microservices based Serverless Application:**

ibmcloud ce application create --name prodlist --image us.icr.io/${SN_ICR_NAMESPACE}/prodlist --registry-secret icr-secret --port 5000 --build-context-dir products_list --build-source https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git

ibmcloud ce application create --name dealerdetails --image us.icr.io/${SN_ICR_NAMESPACE}/dealerdetails --registry-secret icr-secret --port 8080 --build-context-dir dealer_details --build-source https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git

ibmcloud ce application create --name frontend --image us.icr.io/${SN_ICR_NAMESPACE}/frontend --registry-secret icr-secret --port 5001 --build-context-dir products_list --build-source .








