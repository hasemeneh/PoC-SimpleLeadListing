1. How would you scale this sytem to:
- 1M+ leads
- Multiple enrichment providers
- CRM integrations
- Campaign automation
2. Team and Process
if you joined AI Sales Doctor:
- First 90-day engineering priorities
- Team structure (who to hire first), assuming you are the only engineer now
- Dev process (CI/CD,review,release)
3. Tradeoffs
Q: what shortcuts did you take due to time ?
A: Use AI heavily to write the code use an existing template. minimum code change to the template

## 1. System Scaling

How would you scale this system to support:

- **1M+ leads**
- **Multiple enrichment providers**
- **CRM integrations**
- **Campaign automation**

Answer: 

- **1M+ leads** : First of all use the standard kubernetes scaling for the backend. we can also utilize indexing if using relational database or ditch it all together and go for nosql for faster query, as for the front end make sure you have paginated the system so it'll load a rational amount of data each load.
- **Multiple enrichment providers** : Create an abstraction layer can be a service or something that handle the enrichment from each providers and translate it to a common format for our system
- **CRM integrations**: have standarize swagger for easier documentation and documentation discipline for the engineer to document their endpoint enabling other CRM to connect with us. and dedicated document for customer to do integrations with us detailing step by step on how to do it. there's also an option to create SDK but it'll be costly so I forego that option
- **Campaign automation**: create a robust service that handles campaign. we can provide set of available campaign mode supported for our customer and let them customize the campaign and schedule it for later use. kinda like making a draft then execute it only when it's already scheduled till the scheduled time end
---

## 2. Team and Process

If you joined **AI Sales Doctor**:

### First 90-Day Engineering Priorities
Answer : 
- Understand the current system, Company Goal, Product Trajectory, Budget and Expectation within the time limit
- Communicate with stakeholder such as product Owner or anyone in charge of the above topic
- Make an List of possible solution to achieve the goal such as
    - Hiring Plan
    - Team Composition
    - Engineering Budget allocation Proposal (man power and tech stack)
    - Synced Timeline with product owner
- List Down all the thing that we can do in a timely manners 

### Team Structure (Starting as the Only Engineer)
- Hire a **Product Person** if there's none  
- Hire a **UI/UX** if there's none  
- Hire a **backend engineer** to make the backend first can be a junior to save budget  
- Hire a **Senior frontend engineer** to make up for my lack of frontend expertise 
- Hire **QA Engineer** to make sure the product is up to the standard 
- Later add **DevOps / SRE** support to help me maintaining the infrastructure

### Development Process
- Assessment by Engineering Lead and UI/UX
    - Assess the idea and requirement from the Product Person
- Task Breakdown 
    - Break down by Engineering Lead and Senior Engineer 
    - Technical specification depending on the time budget
- Sprint Planning
- Actual Development
- Code reviews
    - Code Reviews done by other
    - Implement sonarqube to see code unit test coverage
    - Implement strict linting for readability
- Release strategy
    - use local, dev and production for initial stage to save cost.  later we can add staging or canary release if we have the budget
    - always do smoke testing
    - implement automation later when possible
    - apply rolling update whenever possible there's many ways to do this depending on the existing system
- Retrospective 
    - Gather Feedback from everyone
---

## 3. Tradeoffs

**Q: What shortcuts did you take due to time constraints?**

**A:**  
- Used AI heavily to generate code  
- Started from an existing template  
- Made minimal code changes to the template