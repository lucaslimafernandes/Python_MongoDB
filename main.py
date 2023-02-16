# Lucas Lima Fernandes
# lucas.lfernandes@live.com

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['teste']

colecao = db['teste_colecao']

documento = {'nome': 'Davi', 'idade': 6}

filtro = {'nome': 'Lucas'}
upd = {'$set': {'idade': 30}}

def inserto(item):

    colecao.insert_one(item)


def selecto():

    documentos = colecao.find({
        'idade': {'$gt': 1}
    })

    return [x for x in documentos]


def updato(filtro, upd):
    """
        filtro = {'nome': 'Lucas'}
        upd = {'$set': {'idade': 29}} 
    """
    colecao.update_one(filtro, upd)


def deleto(filtro):
    """
        filtro = {'nome': 'Davi'}
    """
    colecao.delete_one(filtro)

#print(selecto())

#updato(filtro, upd)
#deleto({'nome': 'Davi'})
inserto(documento)
print(selecto())