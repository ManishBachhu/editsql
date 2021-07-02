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



nltk.download('punkt')
def read_json(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data
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
    sql_q = sql_q[1:-5] + " from student"
    return sql_q


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

