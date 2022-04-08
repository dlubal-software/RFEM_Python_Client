from RFEM.initModel import Model


class PrintoutReport():
    """
    Printout report class encopassing available printout report methods.
    """

    @staticmethod
    def delete(id_list):
        """
        Delete printout report
        """
        Model.clientModel.service.delete_printout_reports(id_list)

    @staticmethod
    def export(report_id: int, target_file_path: str):
        """
        Export printout report to a file.
        """
        Model.clientModel.service.export_printout_report_to_file(
            report_id, target_file_path)

    @staticmethod
    def getList():
        """
        Get list of printout reports.
        """
        return Model.clientModel.service.get_list_of_printout_reports()[0]

    @staticmethod
    def print(printout_report_id: int = 1):
        """
        Print printout report.
        """
        Model.clientModel.service.print_printout_report(printout_report_id)
