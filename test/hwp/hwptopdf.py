# 요건에 맞게 약간 수정 원본: https://github.com/skytreesea/hwp-automation/blob/master/youtube/2%EA%B0%95_PDF%EC%9D%BC%EA%B4%84%EC%A0%80%EC%9E%A5/2_hwp_to_pdf.py
# 보안모듈 다운 받아야 함. https://www.hancom.com/board/devdataView.do?board_seq=47&artcl_seq=4085&pageInfo.page=&search_text=
# 보안모듈 등록해야 함(방법): https://everyday-tech.tistory.com/entry/%EC%95%84%EB%9E%98%ED%95%9C%EA%B8%80-%EC%9E%90%EB%8F%99%ED%99%94-%EB%B3%B4%EC%95%88%EB%AA%A8%EB%93%88-%EB%93%B1%EB%A1%9D
# 실행시 주의사항: 해당 폴더에 한글 파일 이외 다른 파일이 있으면 안됨. 
import os, re  # .path.join(), .listdir(), .chdir(), .getcwd() 등 사용
import time
import win32com.client as win32  # 한/글 열 수 있는 모듈
import win32gui  # 창 숨기기 위한 모듈
BASE_DIR = r'C:\Users\ERC\Documents\파이썬\test\hwp\hwp_file'  # 한글파일이 담긴 경로, 따옴표 앞에 r을 꼭 붙일 것
os.chdir(BASE_DIR)
hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')  # 한/글 열기
hwnd = win32gui.FindWindow(None, '빈 문서 1 - 한글')  # 해당 윈도우의 핸들값 찾기

win32gui.ShowWindow(hwnd, 5)  # 한/글 창을 숨겨줘. 0은 숨기기, 5는 보이기, 3은 풀스크린 등
hwp.RegisterModule("FilePathCheckDLL", "safe")  # 보안모듈 적용

for i in os.listdir():
    if re.search('\.hwp',i):
        hwp.Open(os.path.join(BASE_DIR,i))  # 한글로 열어서
        hwp.HAction.GetDefault('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)  # PDF로 저장, 설정값은 아래와 같이.
        hwp.HParameterSet.HFileOpenSave.filename = os.path.join(BASE_DIR,i.replace('.hwp', '.pdf'))  # 확장자는 .pdf로,
        hwp.HParameterSet.HFileOpenSave.Format = 'PDF'  # 포맷은 PDF로,
        hwp.HAction.Execute('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)  # 위 설정값으로 실행

hwp.XHwpDocuments.Close(isDirty=False)  # 열린 문서가 있다면 묻지 말고 닫아주삼
hwp.Quit()  # 한/글 종료

del hwp
del win32
 