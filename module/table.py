from module import *


class Table:

    def __init__(self, page: Page, only_text: str = '', table_index: int = -1):
        self.page = page
        self.page.wait_for_load_state('networkidle')
        self.table_div = self.page.locator('.bscrmCSS-spin-container>.MT_containers').filter(has_text=only_text).nth(
            table_index)
        self.table_header_tr = self.table_div.locator('//thead/tr').first

    def get_header_locator(self) -> Locator:
        return self.table_header_tr.locator('th')

    def get_header_index(self, header: str) -> int:
        return self.get_header_locator().all_text_contents().index(header)

    def get_row_locator(self, row_locator_or_row_text) -> Locator:
        if isinstance(row_locator_or_row_text, Locator):
            return self.table_div.locator("tr").filter(has=row_locator_or_row_text)
        else:
            return self.table_div.locator("tr").filter(has_text=row_locator_or_row_text)

    def get_cell_locator(self, header: str, row_locator_or_row_text) -> Locator:
        column_index = self.get_header_index(header)
        row_locator = self.get_row_locator(row_locator_or_row_text)
        return row_locator.locator('td').nth(column_index)

    def get_row_dict(self, row_locator_or_row_text) -> dict:
        tr_locator = self.get_row_locator(row_locator_or_row_text)
        td_text_list = tr_locator.locator('td').all_text_contents()
        header_text_list = self.get_header_locator().all_text_contents()
        row_dict = dict(zip(header_text_list, td_text_list))
        return row_dict

    def get_column_list(self, header: str) -> list:
        index = self.get_header_index(header)
        all_tr_locator_list = self.page.locator('//div[@class="bscrmCSS-table-scroll"]//tbody').locator("tr").all()
        column_list = []
        for tr_locator in all_tr_locator_list:
            column_list.append(tr_locator.locator('td').nth(index).text_content())
        return column_list