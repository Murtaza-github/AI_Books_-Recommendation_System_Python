from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# AiBooks module imported to get books recommendation by book name provided by the user.
import AiBooks
# AiBook module imported to get books recommendation by books category selected by the user.
import AiBookType


class System:
    def __init__(self):
        # ==============================variables declaration=============================
        window_width = 1000
        window_height = 550
        # back ground color
        bg = "#660066"
        # front ground color
        fg = "#006600"
        color = "white"

        # main window
        self.root = root
        self.root.title("Book Recommendation System")

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # set the position of the window to the center of the screen
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root.resizable(False, False)
        root.config(bg=bg)

        # title
        fnt = "times new roman"
        title = Label(self.root, text="     Book Recommendation System", font=(fnt, 40, "bold"), bg=bg, fg=color)
        title.place(x=155, y=10)

        # ===========================variable ends========================================

        # ===========================function definition====================================


        def clear_text():
            book_name_entry1.delete(0, END)
            show_books.configure(state="normal")
            show_books.delete("1.0", "end")
            show_books.configure(state="disabled")

        def get_book():
            show_books.delete("1.0", "end")
            book_name = book_name_entry1.get()
            try:
                book = AiBooks.Recommendation(str(book_name))
                book = AiBooks.DataNamesRec(book)
                s_no = 1
                show_books.configure(state="normal")
                show_books.delete("1.0", "end")
                for recommendedBooks in book:
                    books = ("  {:02d}    | {}\n".format(s_no, recommendedBooks))
                    show_books.insert(END, books)
                    s_no = s_no + 1
                show_books.configure(state="disabled")
            except:
                messagebox.showerror("Book not found", "No such book found \ntry again")

        # =========================Function for second frame=========================
        def get_book2():
            # getting book category
            get_book_category = book_category.get()
            show_books2.configure(state='normal')
            show_books2.delete("1.0", "end")
            books = AiBookType.BookTypeRecommend(get_book_category)
            s_no = 0
            for book_names in books:
                s_no = s_no + 1
                show_books2.insert(END, ("  {:02d}    | {}\n".format(s_no, book_names)))

            show_books2.configure(state='disabled')

        def clear2():
            show_books2.configure(state='normal')
            show_books2.delete("1.0", "end")
            show_books2.configure(state='disabled')
            book_category.configure(state='normal')
            book_category.delete(0, END)
            book_category.configure(state='readonly')

        # =========================second frame function ends===========================

        def view_book_name_frame():
            book_name_frame.pack(fill='both', expand=1)
            book_category_frame.pack_forget()
            welcome_label.pack_forget()
            group_member.pack_forget()

        def view_book_category_frame():
            book_category_frame.pack(fill='both', expand=1)
            book_name_frame.pack_forget()
            welcome_label.pack_forget()
            group_member.pack_forget()

        # =======================functions ends=================================

        # Main Button Frame
        main_button_frame = Frame(self.root, bg=fg)
        main_button_frame.place(width=148, height=550)

        book_name_button = Button(main_button_frame, text="Book By Name", bg=bg, fg=color, activebackground=color,
                                  activeforeground=fg, font=(fnt, 12, "bold"), command=view_book_name_frame,
                                  cursor="hand2")
        book_name_button.grid(row=0, column=0, padx=5, pady=20, ipadx=11, sticky="w")

        book_category_button = Button(main_button_frame, text="Book By Category",
                                      bg=bg, fg=color, activebackground=color,
                                      activeforeground=fg, font=(fnt, 12, "bold"), command=view_book_category_frame,
                                      cursor='hand2')
        book_category_button.place(x=5, y=60)

        main_frame1 = Frame(self.root, bg=bg)
        main_frame1.place(x=152, y=75, width=840, height=470)

        welcome_label = Label(main_frame1, text="WELCOME\nARTIFICIAL\n INTELLIGENCE \nPROJECT", bg=bg, fg=fg,
                              font=(fnt, 50, "bold"))
        welcome_label.pack(fill=BOTH, expand=YES)

        group_member = Label(main_frame1, text="Teacher (Maam Farheen Qazi)\n" 
                                               "GROUP MEMBERS\n"
                                               "Murtaza Lakhani (SE-2020-053)\n"
                                               "Ahsan Mumtaz (SE-2020-058)\n"
                                               "Omer Jangeer (SE-2020-064)\n"
                                               "Ali Rashid (SE-2020-065)\n", bg=bg, fg=color,
                             font=(fnt, 14, "bold"))
        group_member.pack(fill=BOTH, expand=YES)
        # ========================== Main Frame ends ======================================

        # ======================== Book by name Frame ====================================
        book_name_frame = Frame(main_frame1, bg=bg)

        # entry frame
        entry_frame = Frame(book_name_frame, bg=bg)
        entry_frame.place(width=850, height=45)

        book_name_label1 = Label(entry_frame, text="Book Name", bg=bg, fg=color, font=(fnt, 20, "bold"))
        book_name_label1.grid(row=0, column=0, pady=5, padx=10)

        book_name_entry1 = Entry(entry_frame, font=(fnt, 12, "bold"), bd=5, fg=color, bg=bg, relief=SUNKEN)
        book_name_entry1.grid(row=0, column=1, padx=0, ipadx=250, columnspan=25)

        # button frame
        button_frame = Frame(book_name_frame, bg=bg)
        button_frame.place(x=160, y=47, width=600, height=35)

        search_book = Button(button_frame, text="Search Book", bg=fg, fg=color, activebackground=color,
                             activeforeground=fg, font=(fnt, 12, "bold"),
                             command=get_book)
        search_book.grid(row=0, column=0, sticky="w")

        clear_search = Button(button_frame, text="Clear Search", bg=fg, fg=color, activebackground=color,
                              activeforeground=fg, font=(fnt, 12, "bold"), command=clear_text)
        clear_search.grid(row=0, padx=5, column=1, sticky="w")

        # recommendation frame
        recommendation_frame = Frame(book_name_frame, bg=bg)
        recommendation_frame.place(y=83, width=845, height=390)

        title = Label(recommendation_frame, text="Book Recommended For User", font=(fnt, 20, "bold"), bg=bg, fg=color)
        title.place(x=250, y=5)

        # table frame tree view
        table_frame = Frame(recommendation_frame, bg=bg, relief=SUNKEN,
                            highlightthickness=2, highlightbackground="white")
        table_frame.place(x=8, y=45, width=830, height=340)

        heading = Label(table_frame, text="S.NO | BOOK NAME", bg=fg, fg=color, font=(fnt, 14, "bold"), anchor='w')
        heading.pack(side=TOP, fill=X, expand=YES)

        show_books = Text(table_frame, width=80, height=17, bg=bg, fg=color, font=(fnt, 14, "bold"),
                          state='normal')
        show_books.pack(side=TOP, fill=BOTH, expand=YES)

        # =============================Book by name frame end=========================================

        # =============================Book by Category Frame=========================================
        book_category_frame = Frame(main_frame1, bg=bg)

        # entry frame
        entry_frame2 = Frame(book_category_frame, bg=bg)
        entry_frame2.place(width=850, height=45)

        find_book2 = Label(entry_frame2, text="Book Category", bg=bg, fg=color, font=(fnt, 20, "bold"))
        find_book2.grid(row=0, column=0, pady=5, padx=10)

        book_category = ttk.Combobox(entry_frame2, font=(fnt, 12), state='readonly')
        book_category['values'] = ("Classic", "Action", "Fantasy", "Horror", "Fiction")
        book_category.grid(row=0, column=1)

        search_book2 = Button(entry_frame2, text="Search Book", bg=fg, fg=color, activebackground=color,
                              activeforeground=fg, font=(fnt, 12, "bold"),
                              command=get_book2)
        search_book2.grid(row=0, column=2, padx=5)

        clear_search2 = Button(entry_frame2, text="Clear Search", bg=fg, fg=color, activebackground=color,
                               activeforeground=fg, font=(fnt, 12, "bold"), command=clear2)
        clear_search2.grid(row=0, column=3, sticky="w")

        # recommendation frame
        recommendation_frame2 = Frame(book_category_frame, bg=bg)
        recommendation_frame2.place(y=40, width=845, height=428)

        title2 = Label(recommendation_frame2, text="Book Recommended For User", font=(fnt, 20, "bold"), bg=bg, fg=color)
        title2.place(x=250, y=5)

        # table frame tree view
        table_frame2 = Frame(recommendation_frame2, bg="green", relief=SUNKEN,
                             highlightthickness=2, highlightbackground="white")
        table_frame2.place(x=8, y=45, width=830, height=383)

        heading2 = Label(table_frame2, text="S.NO | BOOK NAME", bg=fg, fg=color, font=(fnt, 14, "bold"), anchor='w')
        heading2.pack(side=TOP, fill=X, expand=YES)

        show_books2 = Text(table_frame2, width=80, height=17, bg=bg, fg=color, font=(fnt, 14, "bold"),
                           state='normal')
        show_books2.pack(side=TOP, fill=BOTH, expand=YES)

        # =============================Book by Category Frame ends================================


if __name__ == '__main__':
    root = Tk()
    Ob = System()
    root.mainloop()
