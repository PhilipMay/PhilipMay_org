# The selection of topic-specific texts from Wikipedia

:::{post} 2024-08-08
:::

For some machine learning tasks, you want to obtain texts on specific topics.
For example, as a basis for a DPR or RAG training data set.
But which texts can be used? Especially for non-English texts?
And how can they be filtered by topic?

:::{figure} /\_static/img/blog-2024/wp-training-data.png
:width: 550px
:::

## Wikipedia as a source

When it comes to the topic of freely usable texts of high quality and in different languages,
the first choice is Wikipedia.
These two hugging face datasets are suitable as a very good cleaned basis:

1. [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia)
2. [Cohere/wikipedia-22-12-[language]-embeddings](https://huggingface.co/Cohere)

The first data set is the cleaned raw data from Wikipedia.
The second from Cohere is an already split data set with embeddings (which can simply be ignored / deleted).

But how do you filter them by topic?

## Topic filtering

Wikipedia has tons of articles about historical events or other topics that might be far outside your target domain.
This means that you want to select the texts or articles specifically by topic.

Every Wikipedia article is assigned to at least one so-called category.
Each of these categories is in turn assigned to at least one other category
(except the [root category](https://en.wikipedia.org/wiki/Category:Contents)).
Ultimately, this system now forms a [directed acyclic graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph)
from categories with articles as leaves.

The steps are as follows:

1. select certain categories in whose leaves your relevant articles are located
2. retrieve the list of article IDs that are directly or indirectly assigned to these categories
3. use the list of article IDs to select the relevant texts in the data records

## Category selection

As a first step you have to select the categories. This can be one single category or multiple categories.
The easiest way is to first look for a Wikipedia article that is representative of the category.
For example, if the desired category is "everything with mobile devices", then
[iPhone](https://en.wikipedia.org/wiki/IPhone) would be a good starting point.

Now scroll to the bottom of the iPhone Wikipedia page.
A box there shows which categories the article belongs to.
Now click on a suitable category and work your way down the DAC towards the root.
In the case of the iPhone, this would be [Category:iPhone](https://en.wikipedia.org/wiki/Category:IPhone).

Now repeat this process further towards the root of the categories until you have arrived at the appropriate category.
In our case, this would be [Category:Smartphones](https://en.wikipedia.org/wiki/Category:Smartphones),
for example.

## Usage of PetScan

Once you have found one or more relevant categories, you can use [PetScan](https://petscan.wmcloud.org/)
to retrieve the corresponding article IDs. This is done in the following steps:

### 1. Select the language

In PetScan you can select the language in two places.
At the top of the navigation bar you can change the language of the web interface.
This setting does not matter here. The important setting is a little further down in the form.
The Wikipedia language must be set here under "Language".
You will find the correct value as part of the Wikipedia URL.
For German, this is `https://de.wikipedia.org/`.
The correct value for the language is therefore `de`.

### 2. Enter the category / categories

Now we have to enter the categories in the "Categories" field.
One or several separated by a line break.

The format of the category is important at this point.
For example, if the URL of the category is <https://en.wikipedia.org/wiki/Category:Mobile_computers>,
then the correct value for this field is `Mobile_computers`.
While `Mobile computers` would be incorrect.

### 3. Make the remaining entries

Now change the "Depth" field to 20 and
the "Combination" field to "Union".

### 4. Start the search

Now click "Do it!" to get the list of article IDs.

At this point it could be important to see exactly how many results you have. If there are too many, this could be an indication that the category has been selected too broadly. The measure would be to choose a category that is closer to the leaves of the category tree.

### 5. Download the data as a CSV file

In order to be able to process the data automatically,
we want to download it as a CSV file.
To do this, we need to switch to the "Output" tab at the top.
Here we change the "Format" to CSV.
Then we click "Do it!" again and the download will start.

## Select the data

Now we can use the IDs from the "pageid" column to select the Wikipedia texts of the corresponding data sets.
