from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String

# create engine 
engine = create_engine('sqlite:///progLang_ques.db')

# establish session 
Session = sessionmaker(bind=engine)
session = Session()

# declare base 
Base = declarative_base()  # base to store data

class progLang(Base):
    __tablename__ = 'ProgrammingLanguageQuestions'

    language_id = Column(Integer, primary_key=True)
    language_name = Column(String(20))
    language_question = Column(String(256))

Base.metadata.create_all(engine)

# Create language-question data
lang1 = progLang(language_name='python', language_question= 'foo for python?')
lang2 = progLang(language_name='C++', language_question='bar for C++')

lang_list = [lang1,lang2]

session.add_all(lang_list)

session.commit()

if __name__=='__main__':
    # clean the session and test the code
    session.expunge_all()
    langs = session.query(progLang).all()
    langsq= [lang.language_name for lang in langs]

    print len(langsq)








