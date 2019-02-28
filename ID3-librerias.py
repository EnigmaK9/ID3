from id3 import Id3Estimator, export_graphviz
import numpy as np
import graphviz

feature_names = ["No. de ejemplares","Nivel de ventas","Precio"]

x = np.array([["<=4", "Buenas", "<=150"],
	[">4", "Buenas", ">150"],
	[">4", "Buenas", "<=150"],
	["<=4", "Buenas", ">150"],
	[">4", "Buenas", ">150"],
	[">4", "Bajas", ">150"],
	["<=4", "Bajas", ">150"],
	["<=4", "Bajas", ">150"],
	[">4", "Bajas", "<=150"],
	["<=4", "Bajas", "<=150"],
	["<=4", "Promedio", "<=150"],
	[">4", "Promedio", "<=150"],
	["<=4", "Promedio", ">150"],
	[">4", "Promedio", ">150"],
	[">4", "Promedio", "<=150"]])

y = np.array(["si",
	"si",
	"si",
	"si",
	"si",
	"si",
	"no",
	"si",
	"si",
	"no",
	"no",
	"no",
	"si",
	"si",
	"no"])

id3 = Id3Estimator()
id3.fit(x, y)

export_graphviz(id3.tree_, 'librerias.dot', feature_names)
with open("librerias.dot") as f:
	dot_graph = f.read()
g = graphviz.Source(dot_graph)
g.render()
g.view()
