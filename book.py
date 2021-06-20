class Books(object):
    def __init__(self,name,author,pages,color,subject):
        self.name=name
        self.author=author
        self.pages=pages
        self.color=color
        self.subject=subject
    
RD_Sharma = Books('book','agastya',300,'blue','maths')
print(RD_Sharma)


