# coding:utf-8
import pymysql

import settings


class DB():
    def __init__(self):
        self.db = pymysql.connect(**settings.DATABASE.get('default'))
        self.cursor = self.db.cursor()

    def save(self, item):
        if self.exists('user', item.id):
            return
        print(item.img, item.home)

        try:
            self.cursor.execute('insert user(id,name,age,img,home) values(%s,%s,%s,%s,%s)',
                                    args=(item.id, item.name, item.age, item.img, item.home))
            if self.cursor.rowcount:
                print(item.name, '数据保存成功')
                self.db.commit()
        except:
            #回滚
            self.db.rollback()
            print(item.name,'数据保存失败，请重试')

    def exists(self, itableName, id):
        self.cursor.execute('select id from {} where id=%s'.format(itableName), args=(id,))
        # self.cursor.fetchall()
        return self.cursor.rowcount >= 1

    def close(self):
        self.db.close()
