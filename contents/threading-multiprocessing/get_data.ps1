if [ ! -d “./data” ] 
then
 mkdir ./data
 echo ‘created folder ./data’
fi
# get the data if not present:
if [ ! -f “./data/clickstream_data.tsv” ]; then
 if [ ! -f “./data/clickstream_data.tsv.gz” ]
 then
 wget https://dumps.wikimedia.org/other/clickstream/2018-12/clickstream-enwiki-2018-12.tsv.gz -O ./data/clickstream_data.tsv.gz
 fi
 gunzip ./data/clickstream_data.tsv.gz
fi