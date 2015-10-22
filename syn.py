import synapseclient

syn = synapseclient.Synapse()
syn.login()


#library(synapseClient)
#library(plyr)

#synapseLogin()

q = 'select id, UID FROM file WHERE projectId == "syn1773109" AND dataType == "miRNA" AND fileType == "expr"'
qr = syn.query(q)

print type(qr)

#synIds <- res$file.id

#objs <- mlply(synIds, synGet, downloadFile=F, .progress='text')

#mapping <- lapply(objs, function(x) list(id=x@properties$id, state=x@annotations$CellDiffState))

#print(sprintf("State: %s, type: %s, id: %s", f@annotations$CellDiffState,f@annotations$exclude, fid))
                
#syn.get('syn1906480', downloadFile=False)

