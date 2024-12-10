# Journalist-Focused-Causal-Narrative-Explorer

# Outputs

<img width="1349" alt="Screenshot 2024-12-09 at 9 53 36 PM" src="https://github.com/user-attachments/assets/47ec43d7-d24e-40c9-a376-a162758649af">

This image represents a dynamic causal graph illustrating relationships between events extracted from Reuters news articles. Each node in the graph represents a specific event enriched with its associated sentiment—positive, neutral, or negative—while the edges depict causal connections inferred from the text. The visualization provides a storytelling perspective, showing how one event can lead to or influence another, capturing global events' interconnectedness through natural language processing and network analysis.



<img width="967" alt="Screenshot 2024-12-09 at 9 54 32 PM" src="https://github.com/user-attachments/assets/21b6ea43-fcbb-4cd1-a004-24c3e1ddaa91">

This image presents a constructed timeline of events using a climate dataset related to disasters and significant environmental milestones. It includes dates and times for various events, highlighting key historical moments, scientific advancements, and climate-related impacts. The timeline serves as a visual representation of data that can be utilized for climate research, disaster analysis, and environmental studies.




[Watch the video](https://github.com/user-attachments/assets/77509f1e-1af6-4674-8b9a-5648503c3a21)
It is the construction and visualization of causal chains from a given dataset, showcasing relationships between variables. The code generates a causal graph, where nodes represent entities or events and directed edges indicate causal relationships. This structure helps visualize how one event influences another, making complex causal dependencies easier to understand. The output of the analysis is a video that illustrates the evolution of these causal chains.

The video animation plays through 120 frames at 30 frames per second, effectively demonstrating the step-by-step emergence of causal relationships within the data. The visual representation is designed to highlight key pathways, helping users see not only individual causal links but also how they connect to form larger chains. This visual approach aids in interpreting the data and making informed decisions based on the identified causal structures.


# Finalizing the Problem Statement: A Journey Through Literature and Gaps

## 1. Introduction
Event extraction is a critical task in natural language processing (NLP) with applications spanning journalism, crisis management, and decision-making. Extracting events from unstructured text enables organizations to gain insights into trends, relationships, and outcomes in diverse domains like healthcare, finance, and public safety.

Despite advancements, existing methods often struggle with identifying the underlying causality of events — answering the "why" rather than just the "what." This document outlines the journey to refine a problem statement addressing this gap, based on a rigorous review of existing literature and identification of key research gaps.

## 2. Initial Problem Statement
Organizations face challenges analyzing vast amounts of unstructured text, such as news articles and social media. These limitations hinder monitoring trends and making data-driven decisions. Manual event extraction is time-intensive and error-prone, while automated methods are essential for identifying event types, participants, timestamps, and relationships for timely, insightful analysis in finance, healthcare, and public safety.

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
  - Most systems are effective at identifying “what” happened but fall short of understanding “why” events occur.
  - Challenges include linking multiple related events across sentences or documents and detecting nuanced event relationships.

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
- Leverage fine-tuning techniques to enhance detection of nuanced causal indicators like “caused by” or “led to,” improving recall and precision.

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
- Offer narrative views of event chains, enabling storytelling in domains like journalism or crisis reporting.


