from . import schemas,models


def add_emp(request : schemas.Employee, db : models.Emp):
    new_emp = models.Emp(
        name = request.ename,
        desig = request.designation,
        present = request.present,
        doj = request.doj
        )
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_all_emp(db : models.Emp):
    emps = db.query(models.Emp).all()
    return emps

def show_emp(empid : int, db : models.Emp):
    emp = db.query(models.Emp).filter(models.Emp.id == empid).first()
    return emp
