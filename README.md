**Insurance Portal - Microservices Integration** 

**Overview** 

This repository provides a set of microservices for an Insurance Portal that includes functionalities such as quotation generation, policy management, claim submissions, and documentation services. These services are consumed by both the internal components of the portal and external systems, including email and SMS services provided by another team, as well as corporate booking systems via specific API integrations. 

**Microservices-Insurance Portal** 

1. Quotation Service 
- Functionality: Generates insurance quotations based on user inputs such as insurance type, coverage amount, etc. 
- Route: /api/quotation 
2. Policy Service 
- Functionality: Manages insurance policies. Allows for creation and retrieval of user policies. 
- Route: /api/policies 
3. Documentation Service 
- Functionality: Generates policy documents (e.g., PDF) for users after policy creation. 
- Route: /api/documents 
4. Claims Service 
- Functionality: Allows users to submit and manage insurance claims. 
- Route: /api/claims 
5. Email Service 
- Functionality: Sends emails for insurance-related activities, such as policy creation and claim updates. 
- Route: /api/email 
6. SMS Service 
- Functionality: Sends SMS notifications for insurance activities, such as policy confirmation and claim updates. 
- Route: /api/sms 

**Integration with External Teams** 

Email and SMS Services Integration (Team -6) 

The Insurance Portal integrates with Email and SMS services provided by another team. These services are invoked in the following use cases: 

1. **Email Confirmation:** 

   ` `After a policy is purchased, an email is sent to the user with policy details (e.g., policy ID, coverage amount, premium, document ID). 

- Email Service Route:   /api/email/send-quote-email 
2. **SMS Confirmation:** 

   ` `After a policy is purchased, an SMS is sent to the user with confirmation details (e.g., policy ID, coverage amount, premium). 

- SMS Service Route: /api/sms/send-quote-sms 

Both the Email and SMS services are integrated using their respective API calls after successful insurance transactions, including policy creation and claim submission. 

Corporate Booking Integration (Team- 12) 

In addition to internal integrations, the Insurance Portal's Quotation Service, Policy Service, and Documentation Service are made available to another team working on Corporate Booking. This team utilizes the following microservices to handle insurance-related use cases: 

1. **Quotation Service**: 

   ` `Used by the corporate booking system to generate insurance quotations for employees or customers. The team can call the Quotation Service API to obtain premium calculations based on employee details and coverage requirements. 

- Quotation Service Route: /api/quotation 
2. **Policy Service:** 

   ` `This service is used by the corporate booking system to create and manage insurance policies for employees or customers. The team accesses policy creation functionality to integrate insurance products into their corporate booking flows. 

- Policy Service Route: /api/policies 
3. **Documentation Service:** 

   ` `After a policy is created, the corporate booking system retrieves policy documents (e.g., PDFs) through the Documentation Service to provide them to users or save them for record-keeping. 

- Documentation Service Route: /api/documents 

Setup and Configuration 

1. Clone the repository. 
1. Set up the required services as described in the microservices section. 
1. Ensure external teams have access to the appropriate microservices and API routes. 
