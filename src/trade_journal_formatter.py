class format_journal_entry:
    def __init__(self, ticker, entry_price, last_price, change_percent, entry_dna, comments, dca_level, llm_insights):
        self.ticker = ticker
        self.entry_price = entry_price
        self.last_price = last_price
        self.change_percent = change_percent
        self.entry_dna = entry_dna
        self.comments = comments
        self.dca_level = dca_level
        self.llm_insights = llm_insights

    def format_entry(self):
        return f'''
        Stock: {self.ticker}
        Entry Price: {self.entry_price}
        Last Price: {self.last_price}
        Change %: {self.change_percent}%
        Entry DNA: {self.entry_dna}
        Comments: {self.comments}
        LLM Insights: {self.llm_insights}
        DCA Level: {self.dca_level}
        '''
