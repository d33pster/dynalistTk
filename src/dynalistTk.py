#!/usr/bin/env python3

from tkinter import Tk, Toplevel
from tkinter.ttk import Treeview, Frame, Scrollbar
import tkinter.font as tkfont

class dynalistTk:
    def __init__(self, master: Frame | Tk | Toplevel, headers: list, data: list):
        """_summary_
        class dynaList: initiate class object

        Args:
            master (Tk.Frame | ttk.Frame | Tk | Toplevel): parent frame or Tk window (root window) or Toplevel window (Tk popup)
            headers (list): Column names
            data (list): data to be put
        Data Format:
        data = [
            (value1_row1, value2_row1, ...),
            (value1_row2, value2_row2, ...),
            ...
        ]
        """
        self._parent = master
        self._tree = None
        self._treeheaders = headers
        self._treedata = data
        self._setup_widgets()
        self._build_tree()
    
    def _setup_widgets(self):
        container = Frame(self._parent)
        container.pack(fill='both', expand=True)
        # create tree view with dual scrollbars
        self._tree = Treeview(columns=self._treeheaders, show="headings")
        vsb = Scrollbar(orient='vertical', command=self._tree.yview)
        hsb = Scrollbar(orient='horizontal', command=self._tree.xview)
        self._tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self._tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
    
    def _build_tree(self):
        for col in self._treeheaders:
            self._tree.heading(col, text=col.title(), command=lambda c=col: self._sortby(self._tree, c, 0))
            self._tree.column(col, width=tkfont.Font().measure(col.title()))
        
        for item in self._treedata:
            self._tree.insert('', 'end', values=item)
            for ix, val in enumerate(item):
                col_w = tkfont.Font().measure(val)
                if self._tree.column(self._treeheaders[ix], width=None) < col_w:
                    self._tree.column(self._treeheaders[ix], width=col_w)
    
    def _sortby(self, tree: Treeview, col, descending: int):
        # grab values to sort
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=descending)
        
        for ix, item in enumerate(data):
            tree.move(item[1], '', ix)
        
        tree.heading(col, command=lambda col=col: self._sortby(tree, col, int(not descending)))