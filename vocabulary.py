list1 = [
  {'appear' : '����������'},
  {'issues' : '�������'},
  {'provide' : '�������������'},
  {'define' : '����������'},
  {'respectively' : '��������������'},
  {'corresponding' : ['���������������', '��������']},
  {'footer' : '������ ����������'},
  {'aligned' : '���������'},
  {'brackets' : '������'},
  {'instead' : '������'},
  {'themselves' : '���� ����'},
  {'denotes' : '����������'},
  {'allows' : '���������'},
  {'embed' : '���������'},
  {'advertising' : '�������'},
  {'advertise' : '�������������'},
  {'unifying' : '������������'},
  {'aim' : '����'},
  {'dependable' : '��������'},
  {'commonly' : '������'},
  {'rather' : '������'},
  {'advantage' : '������������'},
  {'abilities' : '�����������'},
  {'plain' : '�������'},
  {'offer' : '�����������'},
  {'property' : '���������'},
  {'certain' : '������������'},
  {'describe' : '���������'},
  {'consumers' : '�����������'},
  {'gracefully' : '������'},
  {'able' : '���������'},
  {'seamless' : ['�������', '���������']},
  {'require' : '���������'},
  {'involves' : '�������� � ����'},
  {'achieve' : '���������'},
  {'deploying' : '�������������'},
  {'behavior' : '���������'},
  {'behavior-driven' : '�������������'},
  {'implement' : ['������������', '�������������']},
  {'both' : '���'},
  {'collaborative' : '����������'},
  {'branching' : '���������'},
  {'occurs' : '����� �����'},
  {'commit' : '���������, ������� � ����'},
  {'issues' : '�������'},
  {'bulk' : ['�������� �����', '�����']},
  {'cognitive' : '��������������'},
  {'parsing' : '������'},
  {'workflows' : '������� ��������'},
  {'either' : ['����', '���']},
  {'compatibility' : '�������������'},
  {'particular' : '����������'},
  {'redundancy' : '������������'},
  {'thus' : ['����� �������', '�������']},
  {'purchase' : ['�������', '������������']},
  {'viable' : '��������������'},
  {'nested' : '���������'},
  {'narrow' : '�����'},
  {'consider' : '�����������'},
  {'decision' : '�������'},
  {'compared' : '�����������'},
  {'evolving' : '�������������'},
  {'versatile' : '�������������'},
  {'notorious' : '�����������'},
  {'cumbersome' : '����������'},
  {'concerning' : '����������'},
  {'however' : '������'},
  {'widespread' : '������ ����������������'},
  {'claiming' : '�������'},
  {'fairly' : '������'},
  {'straightforward' : ['�������', '������', '�����������']},
  {'least' : '����������'},
  {'pleasant' : '��������'},
]

for i in list1:
  for k, v in i.items():
    print(f"{k}", end = '')
    while True:
      try:
        word = str(input(' : '))
        if word in v:
          break         
        else:
          print('Wrong!')
          print(f"{k}", end = '')
      except:
        print('')