
# Finalizing the Problem Statement: A Journey Through Literature and Gaps

## 1. Introduction
Event extraction is a critical task in natural language processing (NLP) with applications spanning journalism, crisis management, and decision-making. Extracting events from unstructured text enables organizations to gain insights into trends, relationships, and outcomes in diverse domains like healthcare, finance, and public safety.

Despite advancements, existing methods often struggle to identify the underlying causality of events—answering the "why" rather than just the "what." This document outlines the journey to refine a problem statement addressing this gap based on a rigorous literature review and identifying key research gaps.

## 2. Initial Problem Statement
Organizations need help analyzing vast amounts of unstructured text, such as news articles and social media. These limitations hinder monitoring trends and making data-driven decisions. Manual event extraction is time-intensive and error-prone, while automated methods are essential for identifying event types, participants, timestamps, and relationships for timely, insightful analysis in finance, healthcare, and public safety.

## 3. Literature Review

### Key Papers Reviewed
| Paper                              | Year | Contribution                                                  | Gaps                                                                 |
|------------------------------------|------|--------------------------------------------------------------|----------------------------------------------------------------------|
| Online News Event Extraction for Crisis Surveillance | 2011 | Efficient event extraction from news articles using surface linguistic patterns. | Simplistic event typing, limited semantic understanding, and issues with relation detection. |
| A Deep Learning Model for Hindi Disaster Domain    | 2018 | Combined CNN and Bi-LSTM for event extraction in low-resource languages. | Misclassified triggers, class imbalance, and linguistic subtleties. |
| Spatiotemporal and Semantic Information Extraction | 2018 | Focused on extracting location and timing of events for crisis monitoring. | Vague geographic terms, dependency on specific sources, and event duplication issues. |
| Enhancing Event Causality Identification          | 2024 | Improved multi-hop causality identification using causal graphs. | Struggles with long-distance dependencies and implicit causality.   |
| Large Language Models and Causal Inference         | 2024 | Explored how causal inference enhances LLM reasoning and explainability. | Computational overhead and limited multimodal application.          |

### Insights Gained from Literature Review
- **Current Limitations in Event Extraction**
  - Most systems effectively identify “what” happened but fail to understand “why” events occur.
  - Challenges include linking related events across sentences or documents and detecting nuanced event relationships.

- **Emerging Themes**
  1. **Integration of Causal Reasoning:** Rarely integrated into current systems to understand relationships between events.
  2. **Support for Storytelling:** Causal event chains can significantly enhance journalism and other fields by enabling narrative-based reporting.

- **Unique Opportunity Identified**
  Combining causal inference methods with event extraction could bridge critical gaps, particularly in handling implicit and complex causal relations.

## 4. Final Problem Statement
"How can causal inference be effectively integrated into automated event extraction systems to determine the ‘why’ behind events, providing actionable insights for domains like journalism, crisis management, and decision-making?"

## 5. Methodology
To address the refined problem, the following methodologies are proposed, leveraging state-of-the-art techniques in causal inference and temporal event extraction:

### 1. Event Trigger and Argument Extraction
- Utilize a deep learning framework with pre-trained language models (e.g., BERT or GPT variants) to identify event triggers and extract associated arguments.
- Leverage fine-tuning techniques to enhance the detection of nuanced causal indicators like “caused by” or “led to,” improving recall and precision.

### 2. Temporal Event Linking and Sequencing
- Implement sequence-based models (e.g., Bi-LSTM or Transformers) to extract temporal relationships between events.
- Use pairwise event comparison to infer chronological order and create temporal graphs.
- Augment temporal links with interval-based reasoning for events with implicit timing information.

### 3. Causal Chain Construction
- Integrate probabilistic models like Bayesian Networks or Neural Causal Models to construct multi-hop causal chains.
- Employ multi-task learning frameworks to jointly model temporal and causal relationships, reducing dependencies on annotated datasets.

### 4. Graph-Based Representations for Causal Analysis
- Represent extracted events and their causal or temporal links using directed acyclic graphs (DAGs).
- Incorporate causal reasoning algorithms to resolve long-distance dependencies and implicit causalities across documents.
- Develop scalable graph-based frameworks to manage large datasets efficiently.

### 5. Visualization and User Interaction
- Use visualization libraries (e.g., D3.js, Plotly) to generate interactive causal graphs.
- Provide dynamic features like zooming, filtering, and node highlighting for better user exploration.
- Offer narrative views of event chains, enabling storytelling in journalism or crisis reporting domains.
  
### 6. Retrieval-Augmented Generation (RAG) Integration
- Enhanced Information Retrieval: Combine generative models with retrieval systems to fetch relevant information from indexed documents, ensuring accurate and contextually appropriate responses.
- Contextual Answer Generation: Utilize retrieved data to provide detailed and informed answers, improving the quality and reliability of user interactions.
- Source Attribution: Include references to original sources in generated responses, enhancing transparency and trustworthiness.
- Scalable and Efficient Retrieval: Implement optimized retrieval mechanisms to handle large datasets, maintaining fast and reliable performance as the knowledge base grows.
  

# Journalist-Focused-Causal-Narrative-Explorer

# Outputs

<img width="1349" alt="Screenshot 2024-12-09 at 9 53 36 PM" src="https://github.com/user-attachments/assets/47ec43d7-d24e-40c9-a376-a162758649af">

This image represents a dynamic causal graph illustrating relationships between events extracted from Reuters news articles. Each node in the graph represents a specific event enriched with its associated sentiment—positive, neutral, or negative—while the edges depict causal connections inferred from the text. The visualization provides a storytelling perspective, showing how one event can lead to or influence another, capturing global events' interconnectedness through natural language processing and network analysis.



<img width="967" alt="Screenshot 2024-12-09 at 9 54 32 PM" src="https://github.com/user-attachments/assets/21b6ea43-fcbb-4cd1-a004-24c3e1ddaa91">

This image presents a constructed timeline of events using a climate dataset related to disasters and significant environmental milestones. It includes dates and times for various events, highlighting key historical moments, scientific advancements, and climate-related impacts. The timeline serves as a visual representation of data that can be utilized for climate research, disaster analysis, and environmental studies.




[Watch the video](https://github.com/user-attachments/assets/77509f1e-1af6-4674-8b9a-5648503c3a21)
It constructs and visualises causal chains from a given dataset, showcasing relationships between variables. The code generates a causal graph, with nodes representing entities or events and directed edges indicating causal relationships. This structure helps visualize how one event influences another, making complex causal dependencies easier to understand. The analysis output is a video that illustrates the evolution of these causal chains.

The video animation plays through 120 frames at 30 per second, demonstrating the step-by-step emergence of causal relationships within the data. The visual representation highlights key pathways, helping users see individual causal links and how they connect to form larger chains. This visual approach aids in interpreting the data and making informed decisions based on the identified causal structures.

# NewsNavigator - Guiding journalists to accurate insights.

<img width="603" alt="Screenshot 2024-12-10 at 12 47 05 PM" src="https://github.com/user-attachments/assets/a68d80bb-d9f1-4c1d-bd7d-e419e5fc71b0">

NewsNavigator is an AI-driven tool designed to assist journalists in efficiently gathering, processing, and summarizing information from online sources using RAG (Retrieval-Augmented Generation) techniques. By leveraging RAG, the tool retrieves relevant information from provided URLs or indexed documents and combines it with generative AI to deliver precise, contextually relevant answers to user queries. It also fetches real-time related news articles, making it an invaluable resource for journalists to stay updated and create well-informed reports.

The attached image represents the interface of NewsNavigator, highlighting its functionality. Journalists can input URLs to extract information, submit queries to receive precise answers with verified sources, and explore related news articles. This visual demonstrates how the tool integrates RAG to streamline research and provide actionable insights, empowering journalists to access and synthesize critical information for their stories quickly.













