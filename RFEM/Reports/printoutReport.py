from RFEM.initModel import Model

class PrintoutReport():
    """
    Printout report class encopassing available printout report methods.

    TODO: Create printout report US is paused US-8034.
    """

    @staticmethod
    def delete(id_list, model = Model):
        """
        Delete printout report
        """
        model.clientModel.service.delete_printout_reports(id_list)

    @staticmethod
    def exportToHTML(report_id: int, target_file_path: str, model = Model):
        """
        Export printout report to a HTML.
        """
        model.clientModel.service.export_printout_report_to_html(report_id, target_file_path)

    @staticmethod
    def exportToPDF(report_id: int, target_file_path: str, model = Model):
        """
        Export printout report to a PDF.
        """
        model.clientModel.service.export_printout_report_to_pdf(report_id, target_file_path)

    @staticmethod
    def getList(model = Model):
        """
        Get list of printout reports.
        """
        return model.clientModel.service.get_list_of_printout_reports()[0]

    @staticmethod
    def print(printout_report_id: int = 1, model = Model):
        """
        Print printout report.
        """
        model.clientModel.service.print_printout_report(printout_report_id)
