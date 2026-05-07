from flask import Flask, render_template, request, redirect

from database import conectar_banco, criar_tabela

app= Flask(__name__)

criar_tabela()

@app.route("/",methods=["GET","POST"])
def home():

    conexao= conectar_banco()

    if request.method == "POST":

        nome= request.form.get("nome")
        cpf= request.form.get("cpf")
        setor= request.form.get("setor")
        
        conexao.execute(
            """
            INSERT INTO pessoas (nome, cpf, setor)
            VALUES (?, ?, ?)            
            """,
            (nome, cpf, setor)
        )
        conexao.commit()
        return redirect("/")
    
    busca= request.args.get ("busca")

    if busca:
        pessoas= conexao.execute(
            """
            SELECT * FROM pessoas
            WHERE nome LIKE ?
            OR cpf LIKE ?
            OR id = ?
            """,
            (
                f"%{busca}",
                f"%{busca}",
                busca if busca.isdigit() else -1
            )
        ).fetchall()
    else:
        pessoas= conexao.execute(
            "SELECT * FROM pessoas"
        ).fetchall()

    conexao.close()

    return render_template(
        "index.html",
        pessoas=pessoas,
        total=len(pessoas),
        busca=busca
    ) 
@app.route("/excluir/<int:id>")
def excluir(id):

    conexao= conectar_banco()

    conexao.execute(
        "DELETE FROM pessoas WHERE id = ?",
        (id,)
    ) 

    conexao.commit()
    conexao.close()

    return redirect("/")
app.run(debug=True) 