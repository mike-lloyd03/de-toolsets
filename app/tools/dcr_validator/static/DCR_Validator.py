import os
import pandas as pd

def dcr_validator(wo_file, dcr_file):
    '''
    Joins two spreadsheets on TDC PN and saves that file to disc.

    Returns: name of the output file
    '''
    pd.options.mode.chained_assignment = None  # default='warn'

    wo_data = pd.read_excel(wo_file, header=[0, 1])
    wo_data.columns = [
                        f'{i+" " if "Unnamed" not in i else ""}{j}'
                        for i, j in wo_data.columns
                        ]
    dcr_data = pd.read_csv(dcr_file)
    
    saving_dir = os.path.dirname(wo_file)

    # Select WO list and DCR list from spreadsheet data
    wos = wo_data[['ORDER', 'ITEM', 'START DATE']]
    dcrs = dcr_data[['EAR_NO', 'DCR_Number', 'Expedite', 'Disposition', 'Status',
                 'Department', 'TDC_PN']]

    # Remove asterisks and create unique rows for each PN
    dcr_exp = dcrs
    dcr_exp['TDC_PN'] = dcr_exp['TDC_PN'].str.replace(r"'", "").str.split(',')
    dcr_exp = dcr_exp.explode('TDC_PN')

    wos = wos.rename(columns={'ITEM': 'TDC_PN', 'ORDER': 'WORK ORDER'})
      
    # Merge the two dataframe on the TDC_PN
    dcr_w_wo = pd.merge(dcr_exp, wos, on='TDC_PN').reset_index()

    # Group each entry by DCR Number and setify the work orders then merge with
    # the dcr dataframe
    wo_gb_dcr = dcr_w_wo \
        .groupby('DCR_Number')['WORK ORDER'] \
        .apply(set) \
        .reset_index()
    dcr_w_wo = pd.merge(dcrs, wo_gb_dcr, on='DCR_Number')


    # ### Export the data
    output_filename = 'DCRs w WOs.xlsx'
    writer = pd.ExcelWriter(os.path.join(saving_dir, output_filename))
    dcr_w_wo.to_excel(writer, 'DCRs w WOs', index=False)
    writer.save()
    return output_filename
