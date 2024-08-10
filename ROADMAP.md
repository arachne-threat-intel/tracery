# Tracery Roadmap

## Project Mission and Summary
Tracery is an open-source, privacy-focused metasearch engine maintained by Arachne Digital. Forked from the archived searx project, Tracery aggregates search results from over 70 sources without tracking users, empowering individuals, and organisations to gather intelligence privately and securely. As a key part of Arachne Digital’s Cyber Threat Intelligence (CTI) ecosystem, Tracery is committed to community-driven development and continuous updates, aiming to become the leading metasearch engine for privacy-conscious users.

## Milestones

### Milestone 1: Security Testing and Remediation
* Conduct Penetration Testing: Identify security vulnerabilities in the application through comprehensive penetration testing. Collaborate with the assigned penetration tester to perform a detailed security assessment, covering all aspects of the application infrastructure, codebase, and integrations.
* Review and Prioritise Findings: Understand and categorise the security risks identified during the penetration testing. Analyse the findings provided by the penetration tester, categorise them based on severity, and prioritise them for remediation based on potential impact and ease of exploitation.
* Implement Remediation Measures: Address all identified security vulnerabilities to ensure the safety and integrity of the application. Develop and deploy fixes for the identified vulnerabilities, ensuring that each issue is resolved in line with best security practices. 
* Update Security Documentation: Maintain accurate records of the security posture and mitigation steps taken for the application. Document all findings, remediation steps, and testing results, and update the security policy and procedures to reflect any new security practices or lessons learned from the testing process.

### Milestone 2: Transition to Memory Safe Programming
* Comprehensive Codebase Audit: Identify and document all instances of memory-unsafe code. Conduct a thorough audit of the codebase, cataloguing memory-unsafe code and third-party dependencies, particularly those written in languages like C and C++.
* Software Architecture Analysis and Component Prioritisation: Map the architecture of Thread and Tracery to identify and prioritise critical components for migration to memory safe languages. Understand the overall architecture, focusing on security-critical and performance-critical areas, and prioritise components that handle sensitive data or are frequently targeted by attacks.
* Review and Enhance Current Mitigation Strategies: Assess and improve current security practices related to memory safety. Evaluate existing SAST/DAST tools, code reviews, and secure coding guidelines, with a focus on identifying and enhancing measures specifically targeting memory safety.
Development Workflow and Tool Assessment: Ensure that memory safe practices are effectively integrated into the development workflow. Analyse the current CI/CD processes, testing frameworks, and deployment practices to ensure compatibility with memory safe languages and identify necessary adjustments.
* Team Training and Skill Development: Equip the development team with the necessary skills in memory safe programming languages. Assess current team expertise and develop targeted training programs to upskill developers in languages like Rust, Go, and Swift.
* Align with Long-term Business Goals: Ensure the memory safe roadmap aligns with Arachne Digital’s long-term objectives and resource constraints. Integrate the roadmap with business objectives, taking into account budget, time, and personnel constraints, to create a realistic and achievable plan.
* Implementation and Monitoring: Execute the transition to memory safe programming and monitor progress. Begin migrating prioritised components to memory safe languages, continuously monitor progress, and adjust the plan as necessary to ensure successful implementation.

### Milestone 3: Foundations and Community Building
* Search Engine Monitoring: Establish a process for monitoring and maintaining the list of supported search engines, ensuring that Tracery remains up-to-date and functional even as search engines go offline or change APIs.
* Onboarding New Search Engines: Develop a streamlined process for adding new search engines to Tracery, including documentation and tools to make the process easier for contributors. Regularly update the list of supported search engines based on user feedback and technological developments.
* Community Engagement Initiatives: Kick off a campaign to attract contributors by promoting Tracery’s open-source nature and its importance in the privacy-focused search engine space. Host webinars, write blog posts, and engage with privacy-focused forums and communities to raise awareness.

### Milestone 4: Feature Expansion and Stakeholder Engagement
* Public Web Instance Launch: Deploy a public instance of Tracery, making it accessible to a broader audience. Ensure the instance is stable, secure, and user-friendly, with clear documentation and support resources available.
* Community Engagement Initiatives: Kick off a campaign to attract contributors by promoting Tracery’s open-source nature and its importance in the privacy-focused search engine space. Host webinars, write blog posts, and engage with privacy-focused forums and communities to raise awareness.
* Dark Web Search Integration: Begin researching and integrating search engines that can query the dark web, expanding Tracery’s capabilities and appeal. Ensure that these integrations align with Tracery’s privacy and security standards.
* Stakeholder Outreach: Start engaging with major search engines and other relevant stakeholders, seeking their input on Tracery’s development, and exploring potential collaborations. Develop a strategy for incorporating their feedback into the project.

### Milestone 5: Enhancing User Experience
* User Interface Improvements: Refine Tracery’s user interface and experience, making it more intuitive and accessible. Focus on improving search result presentation, filtering options, and overall usability.

### Milestone 6: Scaling and Sustainability
* Scaling Infrastructure: Optimise the infrastructure to handle increased traffic and usage, ensuring that the public instance of Tracery remains performant and reliable as its user base grows.
* Long-term Sustainability Planning: Develop a sustainability plan for Tracery, including potential funding sources, partnerships, and governance structures to ensure its continued development and maintenance.
* Global Outreach and Localisation: Begin efforts to localise Tracery, translating the interface and documentation into multiple languages to support a global user base. Engage with international privacy and open-source communities to broaden Tracery’s reach.

### Milestone 7: Global Recognition
* Positioning as a Leading Metasearch Engine: Work towards positioning Tracery as the de facto metasearch engine for privacy-conscious users. Increase its visibility in relevant publications, forums, and conferences, and continue to build partnerships that enhance its capabilities and reach.
