import datetime
import pandas as pd
import sys


class Factory:
    def __init__(self, factory=''):
        self.factory = factory
        self.listLine = ()

    def set_line(self, lines: list):
        self.listLine = lines


class Calendar:
    def __init__(self, day=''):
        self.day = day
        self.valid = True
        self.settlement = False
        self.week = ''
        self.level = 1


class Line:
    def __init__(self, line=''):
        self.line = line
        self.lineGroup = ''
        self.linePart = ()
        self.rhythm = {}
        self.maxShiftNum = {}
        self.capacity = {}
        self.fixTime = {}
        self.initPart = ''

        self.lock = {}
        self.assignment = {}

    def set_line_part(self, line_part: list):
        self.linePart = line_part

    def set_rhythm(self, rhythm: dict):
        # d, p : rhythm
        self.rhythm = rhythm

    def set_max_shift_num(self, shift_num: dict):
        # d : shift_num
        self.maxShiftNum = shift_num

    def set_shift_capacity(self, capacity: dict):
        # d : capacity
        self.capacity = capacity

    def set_line_fix_time(self, line_fix_time: dict):
        # d : fix time
        self.fixTime = line_fix_time

    def set_init_part(self, part: str):
        self.initPart = part


class Product:
    def __init__(self, part=''):
        self.part = part
        self.changeGroup = ''
        self.priority = 1
        self.minSlotSize = 1
        self.safeInventory = 0
        self.packAmount = 1
        self.type = ''
        self.isBottle = False
        self.isAdvance = False
        self.isDemand = False
        self.initInventory = 0
        self.dailySupply = {}
        self.routing = ''
        self.process = ''
        self.prev = ''
        self.next = ''


class Order:
    def __init__(self):
        self.order = ''
        self.demand = 0
        self.deliveryDay = ''
        self.type = ''
        self.part = ''


class Config:
    def __init__(self):
        self.objPriority = []
        self.mode = 'normal'
        self.fixed = False
        self.lineGroup = False
