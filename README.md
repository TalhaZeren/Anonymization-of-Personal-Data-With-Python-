In this study, a Python-based approach was developed for the anonymization of
personal data. The project was designed to ensure data privacy and to enable the
secure sharing of personal data. In the study, by using anonymization techniques
and integrating auxiliary anonymization libraries, it was aimed to transform
sensitive tabular data so that they would not contain information specific to

individuals.In the research, metrics such as k-Anonymity, l-Diversity, and t-
Closeness were applied to our attributed data, and the anonymity levels of the

datasets were analyzed. Open-source libraries such as Anjana and pycanon were
used as auxiliary libraries to carry out the anonymization processes. These methods
were tested on the Adult dataset, which is frequently used in the literature and is a
comprehensive, large dataset. As a result, an attempt was made to achieve a balance
in anonymization by using different anonymization techniques together.Following
the anonymization, data loss analyses were conducted, and suppression
(baskılama) rates were measured. Using a weighted scoring system and the PSO
(Particle Swarm Optimization) algorithm, our dataset was analyzed to find the most
optimal result for anonymization. The analysis results were then visualized with
graphs.This study aimed to offer an effective method to ensure anonymity in data
privacy-focused projects and contributed to research in this field.


PSO Algorithm
PSO is an optimization algorithm in which a group of "particles" move through the solution space in search of the best solution. Each particle represents a solution and continuously updates its velocity and position in an effort to achieve better results.


https://github.com/user-attachments/assets/1199b91c-5d42-4c79-9b3f-3b539a1892c2



<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/1388ab86-3280-4a02-bb2b-f1497b8780d6" />  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/72d5e5c9-23c8-420c-b38a-7d6ae08ba53e" />


Each particle represents a combination of parameters in the anonymization process. For example, parameters such as the k-anonymity value, generalization range, and suppression rate.

<img width="663" height="346" alt="image" src="https://github.com/user-attachments/assets/c1996ad5-6ea1-4685-b88d-f81c9eb397b2" />


<img width="954" height="441" alt="image" src="https://github.com/user-attachments/assets/e5320671-e82e-46fd-aef3-c5f4489ed108" />


Bu çalışmada, veri seti üzerinde farklı anonimleştirme teknikleri kullanılarak detaylı bir deneysel süreç gerçekleştirilmiştir. Çalışma kapsamında hem PSO (Particle Swarm Optimization) hem de Ağırlıklı Skorlama Sistemi (Weighted Scoring System) ile anonimlik metrikleri değerlendirilmiş ve karşılaştırmalı bir analiz yapılmıştır. Deneysel sürecin tüm adımları, veri seti üzerinde gerçekleştirilen işlemlerden elde edilen sonuçların analizine ve bu sonuçların görselleştirilmesine kadar detaylı bir şekilde planlanmıştır.


<img width="518" height="311" alt="image" src="https://github.com/user-attachments/assets/2561e910-aebf-43af-853f-53c3418a47a0" />

Utility-risk analysis graphs have been used to reveal the balance between information loss and utility in anonymization processes. These graphs comparatively present the suppression rate and NCP (Normalized Certainty Penalty) values.


<img width="518" height="311" alt="image" src="https://github.com/user-attachments/assets/865d33fd-3ac3-4ed3-92f9-8102ab478e22" />


Anonimlik seviyelerini temsil eden k-anonimlik, l-çeşitlilik ve t-yakınlık metrikleri arasındaki farklar, barplot grafikleri ile görselleştirilmiştir. 
<img width="497" height="316" alt="image" src="https://github.com/user-attachments/assets/7b5c172c-7201-4776-84c3-8425f60e95fb" />






