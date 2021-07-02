from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.status import HTTP_404_NOT_FOUND
from .serializers import EditSQLSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json
import sys
from nltk.tokenize import word_tokenize
import nltk
from subprocess import call
import sqlite3
import re



nltk.download('punkt')
def read_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data

def get_data(sql_query):
    #Connecting to sqlite
    conn = sqlite3.connect(
        '/home/ubuntu/uhack/editsql2/editsql/data/database/test_student/test_student.sqlite'
        )
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    names = next(zip(*cursor.description))
    
    return (rows, names)


def edit_json(text):
    file_path = "/home/ubuntu/uhack/editsql2/editsql/data/sparc/dev_no_value.json"
    data = read_json(file_path)
    data[0]["final"]["utterance"] = text
    data[0]["interaction"][0]["utterance"] = text
    data[0]["interaction"][0]["utterance_toks"] = word_tokenize(text)
    with open(file_path, "w") as f:
        f.write(json.dumps(data))
    call('/home/ubuntu/uhack/editsql2/editsql/test_sparc_editsql.sh')
    output_file = '/home/ubuntu/uhack/editsql2/editsql/output.txt'
    with open(output_file, 'r') as f:
        sql_q = f.read()
    sql_q = sql_q[1:-5] + "from Student"
    expr = "\s[a-z]*\.\*\\s"
    expr2 = " * "
    sql_q = re.sub(expr,expr2,sql_q)
    try:
        rows, cols = get_data(sql_q)
    except Exception:
        rows = []
        cols = []
    
    response = {
        "sql_query": sql_q,
        "rows": rows,
        "cols": cols
    }
    return response


class EditSQLView(APIView):
    
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = EditSQLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            text = serializer.data['input_text']
            data = edit_json(text)
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

