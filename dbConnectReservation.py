import sqlite3


class connectdata:
    def __init__(self):
        self._db = sqlite3.connect("reservation.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists ticket (Name text,Gender text, Comments text)")
        self._db.commit()

    def addasd(self, name, gender, comments):
        self._db.row_factory = sqlite3.Row
        self._db.execute("insert into ticket (Name,Gender,Comments) values(?,?,?)", (name, gender, comments))
        self._db.commit()
        return("is added")

    def listasd(self):
        cursor = self._db.execute("select * from ticket")
        for row in cursor:
            print("the Name :{},Gender:{},Comments".format(row["Name"], row["Gender"], row["Comments"]))

    def delrecord(self, name):
        self._db.row_factory = sqlite3.Row
        self._db.execute("delete from ticket where Name = '{}' ".format(name))
        self._db.commit()
        return("is deleted")

    def update(self, name, comments):
        self._db.row_factory = sqlite3.Row
        self._db.execute("update ticket set Comments = ? where Name=?", (comments, name))
        self._db.commit()
        return("is updated")