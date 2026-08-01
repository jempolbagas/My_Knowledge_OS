---
title: "What is Model Context Protocol (MCP)? A guide"
source: "https://cloud.google.com/discover/what-is-model-context-protocol?hl=en"
author:
published:
created: 2026-08-02
description: "Learn how the Model Context Protocol (MCP) standard allows LLMs to safely access external data and use tools, making AI more powerful and reliable."
tags:
  - "clippings"
---
## What is the MCP and how does it work?

[Large language models](https://cloud.google.com/ai/llms) (LLMs) are powerful, but they have two major limitations: their knowledge is frozen at the time of their training, and they can't interact with the outside world. This means they can't access real-time data or perform actions like booking a meeting or updating a customer record.

The Model Context Protocol (MCP) is an open standard designed to solve this. Introduced by [Anthropic](https://cloud.google.com/products/model-garden/claude) in November 2024, MCP provides a secure and standardized "language" for LLMs to communicate with external data, applications, and services. It acts as a bridge, allowing AI to move beyond static knowledge and become a dynamic [agent](https://cloud.google.com/discover/what-are-ai-agents) that can retrieve current information and take action, making it more accurate, useful, and automated.

## Understanding the Model Context Protocol

The MCP creates a standardized, two-way connection for AI applications, allowing LLMs to easily connect with various data sources and tools. MCP builds on existing concepts like tool use and function calling but standardizes them. This reduces the need for custom connections for each new AI model and external system. It enables LLMs to use current, real-world data, perform actions, and access specialized features not included in their original training.

## MCP architecture and components

The Model Context Protocol has a clear structure with components that work together to help LLMs and outside systems interact easily.

### MCP host

The LLM is contained within the MCP host, an AI application or environment such as an AI-powered IDE or conversational AI. This is typically the user's interaction point, where the MCP host uses the LLM to process requests that may require external data or tools.

### MCP client

The MCP client, located within the MCP host, helps the LLM and MCP server communicate with each other. It translates the LLM's requests for the MCP and converts the MCP's replies for the LLM. It also finds and uses available MCP servers.

### MCP server

The MCP server is the external service that provides context, data, or capabilities to the LLM. It helps LLMs by connecting to external systems like databases and web services, translating their responses into a format the LLM can understand which helps developers provide diverse functionalities.

### Transport layer

The transport layer uses JSON-RPC 2.0 messages to communicate between the client and server, mainly through two transport methods:

- **Standard input/output (stdio):** Works well for local resources, offering fast, synchronous message transmission
- **Server-sent events (SSE):** Preferred for remote resources, allowing efficient, real-time data streaming

## How does the MCP work?

At its core, the Model Context Protocol allows an LLM to request help from external tools to answer a query or complete a task. Imagine you ask an AI assistant: "Find the latest sales report in our database and email it to my manager."

Here is a simplified look at how MCP would handle this:

1. **Request and tool discovery:** The LLM understands it cannot access a database or send emails on its own. It uses the MCP client to search for available tools, where it finds two relevant tools registered on MCP servers: a database\_query tool and an email\_sender tool.
2. **Tool invocation:** The LLM generates a structured request to use these tools. First, it calls the database\_query tool, specifying the report name. The MCP client then sends this request to the appropriate MCP server.
3. **External action and data return:** The MCP server receives the request, translates it into a secure SQL query for the company's database, and retrieves the sales report. It then formats this data and sends it back to the LLM.
4. **Second action and response generation:** Now equipped with the report data, the LLM calls the email\_sender tool, providing the manager's email address and the report content. After the email is sent, the MCP server confirms the action was completed.
5. **Final confirmation:** The LLM provides a final response to you: "I have found the latest sales report and emailed it to your manager."

## MCP versus RAG

Both Model Context Protocol (MCP) and [Retrieval-Augmented Generation](https://cloud.google.com/use-cases/retrieval-augmented-generation) (RAG) improve LLMs with outside information, but they do this through different ways and serve distinct purposes. RAG finds and uses information for creating text, while MCP is a wider system for interaction and action.

**Feature**

**Model Context Protocol (MCP)**

**Retrieval-Augmented Generation (RAG)**

Primary goal

Standardize two-way communication for LLMs to access and *interact* with external tools, data sources, and services to perform actions alongside information retrieval.

Enhance LLM responses by *retrieving relevant information* from an authoritative knowledge base *before* generating a response.

Mechanism

Defines a standardized protocol for LLM applications to *invoke external functions* or request structured data from specialized servers, enabling actions and dynamic context integration.

Incorporates an information retrieval component that uses a user's query to pull information from a knowledge base or data source. This retrieved information then augments the LLM's prompt.

Output type

Enables LLMs to *generate structured calls* for tools, receive results, and then generate human-readable text based on those results and actions. Can also involve real-time data and functions.

LLMs generate responses based on their training data *augmented* by text relevant to the query from external documents. Often focuses on factual accuracy.

Interaction

Designed for *active interaction* and execution of tasks in external systems, providing a "grammar" for LLMs to "use" external capabilities.

Primarily for *passive retrieval* of information to inform text generation; not typically for executing actions within external systems.

Standardization

An open standard for how AI applications provide context to LLMs, standardizing integration and reducing the need for custom APIs.

A technique or framework for improving LLMs, but not a universal protocol for tool interaction across different vendors or systems.

Use cases

AI agents performing tasks (for example, booking flights, updating CRM, running code), fetching real-time data, advanced integrations.

Question-answering systems, chatbots providing up-to-date factual information, summarizing documents, reducing hallucinations in text generation.

## Benefits of using the MCP

The Model Context Protocol offers several potential advantages for developing and deploying AI-powered applications, making LLMs more versatile, reliable, and capable.

### Reduced hallucinations

LLMs, by nature, can sometimes make up facts or produce plausible but ultimately incorrect information ([hallucinate](https://cloud.google.com/discover/what-are-ai-hallucinations)) because they predict answers based on training data, not real-time information. The MCP helps reduce this by providing a clear way for LLMs to access external, reliable data sources, making their responses more truthful.

### Increased AI utility and automation

This protocol helps AI do much more and work on its own. Usually, LLMs only know what they were trained on, which can quickly become outdated. However, with MCP LLMs can connect with many ready-made tools and integrations like business software, content repositories, and development environments. This means AI can handle more complicated jobs that involve interacting with the real world, such as updating customer information in a CRM system, looking up current events online, or running special calculations. By directly connecting to these outside tools, LLMs are no longer just chat programs; they become smart agents that can act independently, which means a lot more can be automated.

### Easier connections for AI

Before MCP, connecting LLMs to different external data sources and tools was more difficult, usually needing special connections or using methods specific to each vendor. This resulted in a complicated and messy system, often called the "N x M" problem, because the number of necessary custom connections grew very quickly with every new model or tool. MCP offers a common, open standard that makes these connections easier, much like how a USB-C port makes connecting devices simple. This simpler method can lower development costs, speed up the creation of AI applications, and create a more connected AI environment. Developers can also more easily switch between LLM providers and add new tools without major changes.

## MCP and security

While the Model Context Protocol improves LLM capabilities by connecting them to outside systems, it also can open up important security considerations. As MCP can access any data and potentially run code through connected tools, strong security is essential.

Key security principles for MCP include:

- **User consent and control:** Users need to clearly understand and agree to all actions and data access the LLM performs through MCP. They should be able to control what data is shared and what actions are taken, ideally through easy-to-use authorization screens.
- **Data privacy:** Before exposing user data to MCP servers, hosts must get clear permission from users. Sensitive data should be protected with proper access controls to prevent accidental leaks or sharing, especially since LLMs handle large amounts of data. Using encryption and strong access control rules is essential.
- **Tool safety:** Tools linked through MCP can be used to run code. Developers should not trust tool descriptions unless they come from a reliable server. Users should give permission before any tool is used and understand what the tool does before allowing it to run.
- **Secure output handling:** LLM outputs from MCP interactions must be handled carefully to prevent security problems like cross-site scripting (XSS) or other web application attacks if the output is shown to users. It's important to properly clean up input and filter output, and to avoid including sensitive data in the prompts.
- **Supply chain security:** The reliability of the MCP servers and the external tools they connect to is very important. Organizations should make sure all parts of their LLM supply chain are secure to prevent biased results, security breaches, or failures.
- **Monitoring and auditing:** Regularly checking LLM activity and how it interacts with MCP servers can help find unusual behavior or potential misuse. Setting up strong logging and auditing systems allows tracking of data movement and tool usage, which helps when responding to security incidents.

By sticking to these principles, developers can use the power of MCP while protecting against potential risks.

## Building and deploying an MCP-powered application

Implementing the Model Context Protocol requires a robust infrastructure to host the LLM, the MCP servers, and the underlying data sources. A cloud platform provides the scalable and secure components needed to build a complete solution. Here’s how you can approach it:

### Hosting and scaling your MCP servers

MCP servers are the bridge to your external tools. Depending on your needs, you can choose:

- **Serverless environments (like** [**Cloud Run**](https://cloud.google.com/run)**):** Ideal for simple, stateless tools. A serverless platform automatically scales your servers based on demand—even to zero—so you only pay for what you use. This is perfect for deploying individual tools efficiently.
- **Container orchestration (like** [**Google Kubernetes Engine**](https://cloud.google.com/kubernetes-engine) **(GKE)):** For complex, stateful applications that require fine-grained control over networking and resources, a managed Kubernetes environment provides the power and flexibility needed to run sophisticated MCP infrastructure at enterprise scale.

### Connecting MCP to your data and tools

Much of the value of MCP comes from the tools it can access. You can connect your LLM to:

- **Managed databases (like** [**Cloud SQL**](https://cloud.google.com/sql) **or** [**Spanner**](https://cloud.google.com/spanner)**):** Allow your AI to securely query relational databases for things like customer information, inventory, or operational data
- **Data warehouses (like** [**BigQuery**](https://cloud.google.com/bigquery)**):** For analytical tasks, an LLM can leverage a data warehouse to analyze massive datasets and derive deep, contextual insights in response to a user's query

### Orchestrating the end-to-end AI workflow with Gemini Enterprise Agent Platform

A unified AI platform is essential for tying everything together. [Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) helps you manage the entire life cycle of your MCP-powered application:

- **LLM hosting:** Deploy and manage powerful foundation models like Gemini, which serve as the "brain" of your application.
- **Agent and orchestration frameworks:** Building an AI agent involves complex workflows. Agent Platform provides tools to streamline the flow of information between the LLM and the context provided by your MCP servers, simplifying the development of sophisticated agents that can reason and act.

## The role of open source in MCP

As an open standard, MCP encourages a vibrant ecosystem of open source implementations. Developers can find pre-built MCP server frameworks and libraries in various programming languages, which can significantly accelerate development. Adopting open source MCP components promotes interoperability between different AI models and services, prevents vendor lock-in, and allows your organization to benefit from community-driven innovation and support.

#### Additional resources

- [Fully-managed, remote MCP servers for Google and Google Cloud services](https://docs.cloud.google.com/mcp)
- [Host MCP servers on Cloud Run](https://cloud.google.com/run/docs/host-mcp-servers)
- [Build and deploy a remote MCP Server on Cloud Run](https://cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server)
- [Connect your IDE to Cloud SQL with MCP](https://cloud.google.com/sql/docs/mysql/pre-built-tools-with-mcp-toolbox)