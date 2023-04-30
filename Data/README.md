# Dataset introduction

## LEGO dataset
This project primarily uses the [LEGO dataset](https://github.com/SeventhPrize/INDE_577_Data_Science_and_Machine_Learning/blob/main/Data/Brickset-Most-Owned-Query-33-02042023.csv) obtained from [Brickset](https://brickset.com/sets/query-33). For each LEGO set that has been released (as of Feb 4, 2023), the dataset contains information about the LEGO set's theme, number of pieces, weight, width/height/depth, price, and value.

We primarily explore the LEGO dataset using classification models. Specifically, we try to predict a LEGO set's theme. We care most about the Duplo, Bionicle, and Education themes. The Duplo and Bionicle themes were selected because their sets are very physically distinct: Duplo sets are composed of fewer pieces that are each quite large. They are brightly colored, blocky, and marketed toward young children. By constrast, Bionicle sets are intricate action figures with small, moveable parts. Finally, the Education theme was selected because it introduces several interesting challenges: there are relatively few observations of Education sets in the data leading to an unbalanced dataset; furthermore, the Education sets have a wide range of physical characteristics, which make them challenging to separate from the Duplo and Bionicles sets. Education sets have a heavy emphasis on robotics and include motors, electronic sensors, and programmable bricks.

![Duplo](https://en.wikipedia.org/wiki/Lego_Duplo#/media/File:2_duplo_lego_bricks.jpg)
![Bionicles](https://static.wikia.nocookie.net/bionicle/images/b/b3/Vezok.jpg/revision/latest?cb=20110731003440)
![Education](https://en.wikipedia.org/wiki/File:Lego_Mindstorms_Sound_Finder.jpg)
[Duplo](https://en.wikipedia.org/wiki/Lego_Duplo) (top), [Bionicles](https://bionicle.fandom.com/wiki/Vezok) (middle), and [Education](https://en.wikipedia.org/wiki/File:Lego_Mindstorms_Sound_Finder.jpg) (bottom) sets are shown above.

The [healthcare dataset](https://github.com/SeventhPrize/INDE_577_Data_Science_and_Machine_Learning/blob/main/Data/healthcare-dataset-stroke-data.csv) is used exclusively for the [stroke prediction model](https://github.com/SeventhPrize/INDE_577_Data_Science_and_Machine_Learning/tree/main/Supervised%20learning/Stroke%20prediction).

For some models, we artifically generate data to enable a cleaner demonstration of the model's intent and capabilities.
