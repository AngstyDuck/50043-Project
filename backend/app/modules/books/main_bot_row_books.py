import random
from flask import jsonify, request
from flask import current_app as app
import numpy as np



def _main_bot_row_books():
    print("ping - _main_bot_row_books")
    start = request.args.get("start_list")
    seed = request.args.get("seed")
    seed = 833  # HARDCODED SEED (for now)
    _end = request.args.get("end_list")  # currently unused
    print("start: {0}; end: {1}; seed: {2}".format(start, _end, seed))

    # declare pymysql client
    connection = app.config["PYMYSQL_CONNECTION"]

    # declare pymongo client
    mongo = app.config["MONGODB_CLIENT"]
    metadata = mongo.metadata.metadata

    start = int(start)
    random.seed(int(seed))
    count = int(metadata.count())
    total_lst = random.sample(range(count), count)
    end = start+18
    lst = total_lst[start:end]
    lst = list(np.array(lst,dtype=str))
    print("lst: {0}".format(lst))

    finaldict = {}
    outerlist = []

    met_data = metadata.find( { 'index': { '$in' : lst } }, { '_id':0,'title':1,'asin':1,'imUrl':1,'categories':1,'related':1 } )

    for j in met_data:
        temp = {}

        if 'title' in j:
            temp['title'] = j['title']

        temp['asin'] = j['asin']

        # averageRating = db.session.query(func.avg(amazonreviews.overall)).group_by(amazonreviews.asin).filter_by(asin=j['asin']).scalar()

        # pymysql query
        query = "SELECT AVG(overall) FROM {0} WHERE asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], temp['asin'])
        # with connection as cursor:
        with connection.cursor() as cursor:
            print("query: {0}".format(query))
            cursor.execute(query)
            query_result = cursor.fetchone()
            averageRating = query_result["AVG(overall)"]
            if averageRating:
                averageRating = float(averageRating)

                temp['averageRating'] = averageRating

                if 'imUrl' in j:
                    temp['imUrl'] = j['imUrl']
                else:
                    temp['imUrl'] = None

                temp['categories'] = j['categories']

                final_related_list = []
                if 'related' in j:
                    related = j['related']
                    related_list = []

                    for a in related:
                        for b in related[a]:
                                related_list.append(b)

                    related_results = metadata.find( { 'asin': { '$in': related_list } }, { 'asin':1, 'imUrl':1} )

                    for k in related_results:
                        temp1 = {}
                        temp1['asin'] = k['asin']
                        temp1['imUrl'] = k['imUrl']
                        final_related_list.append(temp1)
                    temp['related'] = final_related_list

                else:
                    temp['related'] = None
                outerlist.append(temp)
                print(temp)
                print("\n\n\n")
            else:
                # print("empty dict")
                # outerlist.append({})
                pass
        cursor.close()

    finaldict['collection'] = outerlist

    # print(lst)
    # print(finaldict)
    # print()
    # print(len(finaldict['books']))
    # print(type(finaldict))

    return(jsonify(finaldict))

def _main_top_row_books():
    print("ping - _main_top_row_books")
    output = {
      "recommended": [
        {
          "title": "Faux Leather Kindle Sleeve Case for Kindle (Fits 9.7&quot; Display, Latest Generation Kindle DX) - Yellow (Smooth finish)",
          "asin": "B002HWRIIQ",
          "averageRating": 4.6,
          "imUrl": "http://ecx.images-amazon.com/images/I/513mtcKv9HL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
          "categories": [
            [
              "Books",
              "Business & Money",
              "Job Hunting & Careers",
              "Guides"
            ],
            [
              "Books",
              "Business & Money",
              "Job Hunting & Careers",
              "Job Hunting"
            ],
            [
              "Books",
              "Business & Money",
              "Job Hunting & Careers",
              "Resumes"
            ],
            [
              "Kindle Store",
              "KindlQe eBooks",
              "Business & Money",
              "Job Hunting & Careers",
              "Career Guides"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Business & Money",
              "Job Hunting & Careers",
              "Job Hunting"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Business & Money",
              "Job Hunting & Careers",
              "Resumes"
            ]
          ]
        },
        {
          "asin": "B002HWRKES",
          "price": 0.99,
          "averageRating": 3.6,
          "imUrl": "http://ecx.images-amazon.com/images/I/51KA6TO1xdL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
          "related": [
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            }
          ],
          "categories": [
            [
              "Books",
              "Christian Books & Bibles"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Religion & Spirituality",
              "Christian Books & Bibles"
            ]
          ]
        },
        {
          "asin": "B002HWRKPM",
          "averageRating": 2.5,
          "description": "A 20 year fan of the Montreal Canadiens, transplanted to the west coast, follows both of his teams the Sharks and the Habs.I obviously have too much free time.Kindle blogs are fully downloaded onto your Kindle so you can read them even when you're not wirelessly connected. And unlike RSS readers which often only provide headlines, blogs on Kindle give you full text content and images, and are updated wirelessly throughout the day.",
          "categories": [
            [
              "Kindle Store",
              "Kindle Blogs",
              "Sports"
            ]
          ]
        },
        {
          "asin": "B002HWRR78",
          "price": 0.99,
          "averageRating": 4.2,
          "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
          "related": [
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            }
          ],
          "categories": [
            [
              "Books",
              "Christian Books & Bibles"
            ],
            [
              "Books",
              "Literature & Fiction",
              "Classics"
            ],
            [
              "Kindle Store",
              "Kindle Short Reads",
              "One hour (33-43 pages)",
              "Religion & Spirituality"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Religion & Spirituality",
              "Christian Books & Bibles"
            ]
          ]
        }
      ],
      "best": [
        {
          "title": "Faux Leather Kindle Sleeve Case for Kindle (Fits 9.7&quot; Display, Latest Generation Kindle DX) - Yellow (Smooth finish)",
          "asin": "B002HWRIIQ",
          "averageRating": 4.6,
          "imUrl": "http://ecx.images-amazon.com/images/I/513mtcKv9HL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
          "categories": [
            [
              "Books",
              "Business & Money",
              "Job Hunting & Careers",
              "Guides"
            ],
            [
              "Books",
              "Business & Money",
              "Job Hunting & Careers",
              "Job Hunting"
            ],
            [
              "Books",
              "Business & Money",
              "Job Hunting & Careers",
              "Resumes"
            ],
            [
              "Kindle Store",
              "KindlQe eBooks",
              "Business & Money",
              "Job Hunting & Careers",
              "Career Guides"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Business & Money",
              "Job Hunting & Careers",
              "Job Hunting"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Business & Money",
              "Job Hunting & Careers",
              "Resumes"
            ]
          ]
        },
        {
          "asin": "B002HWRKES",
          "price": 0.99,
          "averageRating": 3.6,
          "imUrl": "http://ecx.images-amazon.com/images/I/51KA6TO1xdL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
          "related": [
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            }
          ],
          "categories": [
            [
              "Books",
              "Christian Books & Bibles"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Religion & Spirituality",
              "Christian Books & Bibles"
            ]
          ]
        },
        {
          "asin": "B002HWRKPM",
          "averageRating": 2.5,
          "description": "A 20 year fan of the Montreal Canadiens, transplanted to the west coast, follows both of his teams the Sharks and the Habs.I obviously have too much free time.Kindle blogs are fully downloaded onto your Kindle so you can read them even when you're not wirelessly connected. And unlike RSS readers which often only provide headlines, blogs on Kindle give you full text content and images, and are updated wirelessly throughout the day.",
          "categories": [
            [
              "Kindle Store",
              "Kindle Blogs",
              "Sports"
            ]
          ]
        },
        {
          "asin": "B002HWRR78",
          "price": 0.99,
          "averageRating": 4.2,
          "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg",
          "related": [
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            },
            {
              "asin": "B0070YQGSO",
              "imUrl": "http://ecx.images-amazon.com/images/I/51zBsXMfkFL._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg"
            }
          ],
          "categories": [
            [
              "Books",
              "Christian Books & Bibles"
            ],
            [
              "Books",
              "Literature & Fiction",
              "Classics"
            ],
            [
              "Kindle Store",
              "Kindle Short Reads",
              "One hour (33-43 pages)",
              "Religion & Spirituality"
            ],
            [
              "Kindle Store",
              "Kindle eBooks",
              "Religion & Spirituality",
              "Christian Books & Bibles"
            ]
          ]
        }
      ]
    }

    return jsonify(output)
