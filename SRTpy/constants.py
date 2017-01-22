"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

TRAIN_CODE = {
    '00': 'KTX',
    '02': '무궁화',
    '03': '통근열차',
    '04': '누리로',
    '05': '전체', 
    '07': 'KTX-산천',
    '08': '새마을',
    '08': 'ITX-새마을',
    '09': 'ITX-청춘',
    '17': 'SRT',
}

TRAIN_GROUP_CODE = {
    '100': ['KTX', 'KTX-산천'],
    '101': ['새마을', 'ITX-새마을'],
    '102': ['무궁화', '누리로'],
    '103': ['통근열차'],
    '104': ['ITX-청춘'],
    '109': ['ALL', 'all', 'All', '전체'],
    '300': ['SRT'],
    '900': ['SRT+KTX'],
}

STATION_CODE = {
    # SRT
    '0551': '수서',
    '0552': '동탄',
    '0553': '지제',
    # KTX
    '0001': '서울',
    '0104': '용산',
    '0921': '인천공항',
    '0918': '검암',
    '0002': '영등포',
    '0501': '광명',
    '0003': '수원',
    '0502': '천안아산',
    '0297': '오송',
    '0010': '대전',
    '0025': '서대전',
    '0507': '김천구미',
    '0015': '동대구',
    '0515': '포항',
    '0017': '밀양',
    '0019': '구포',
    '0020': '부산',
    '0508': '신경주',
    '0509': '울산',
    '0063': '진주',
    '0059': '마산',
    '0057': '창원',
    '0512': '창원중앙',
    '0056': '진영',
    '0024': '경산',
    '0027': '논산',
    '0514': '공주',
    '0030': '익산',
    '0033': '정읍',
    '0036': '광주송정',
    '0037': '나주',
    '0041': '목포',
    '0045': '전주',
    '0048': '남원',
    '0051': '순천',
    '0053': '여수EXPO',
    '0390': '행신',
    '0218': '계룡',
    '0139': '여천',
    '0050': '구례구',
    '0049': '곡성',
    # all
    '0342': '가수원',
    '0476': '가야',
    '0150': '가평',
    '0309': '각계',
    '0481': '갈촌',
    '0028': '강경',
    '0115': '강릉',
    '0151': '강촌',
    '0482': '개양',
    '0219': '개태사',
    '0160': '개포',
    '0216': '거제',
    '0433': '거촌',
    '0184': '건천',
    '0918': '검암',
    '0024': '경산',
    '0021': '경주',
    '0468': '경화',
    '0218': '계룡',
    '0917': '계양',
    '0240': '고막원',
    '0122': '고한',
    '0049': '곡성',
    '0259': '공전',
    '0514': '공주',
    '0920': '공항화물',
    '0370': '관촌',
    '0491': '광곡',
    '0501': '광명',
    '0068': '광양',
    '0145': '광운대',
    '0042': '광주',
    '0036': '광주송정',
    '0082': '광천',
    '0241': '괴목',
    '0050': '구례구',
    '0013': '구미',
    '0019': '구포',
    '0329': '구학',
    '0323': '국수',
    '0061': '군북',
    '0505': '군산',
    '0208': '굴봉산',
    '0043': '극락강',
    '0736': '금강',
    '0239': '금곡',
    '0732': '금릉',
    '0187': '기장',
    '0246': '김유정',
    '0031': '김제',
    '0012': '김천',
    '0507': '김천구미',
    '0916': '김포공항',
    '0461': '나원',
    '0201': '나전',
    '0037': '나주',
    '0164': '나한정',
    '0131': '남문산',
    '0317': '남성현',
    '0048': '남원',
    '0186': '남창',
    '0152': '남춘천',
    '0497': '남평',
    '0361': '노안',
    '0027': '논산',
    '0391': '능곡',
    '0132': '능주',
    '0266': '다시',
    '0176': '단성',
    '0096': '단양',
    '0247': '달천',
    '0417': '대광리',
    '0023': '대구',
    '0148': '대성리',
    '0310': '대신',
    '0430': '대야',
    '0010': '대전',
    '0083': '대천',
    '0233': '덕산',
    '0168': '덕소',
    '0052': '덕양',
    '0209': '덕하',
    '0111': '도계',
    '0077': '도고온천',
    '0095': '도담',
    '0403': '도라산',
    '0015': '동대구',
    '0410': '동두천',
    '0189': '동래',
    '0450': '동백산',
    '0366': '동산',
    '0364': '동익산',
    '0437': '동점',
    '0552': '동탄',
    '0113': '동해',
    '0173': '동화',
    '0615': '두정',
    '0205': '득량',
    '0915': '디엠씨',
    '0059': '마산',
    '0147': '마석',
    '0038': '망상',
    '0249': '매곡',
    '0235': '명봉',
    '0041': '목포',
    '0074': '목행',
    '0229': '몽탄',
    '0236': '무안',
    '0114': '묵호',
    '0401': '문산',
    '0224': '물금',
    '0244': '미평',
    '0120': '민둥산',
    '0017': '밀양',
    '0327': '반곡',
    '0062': '반성',
    '0738': '백마고지',
    '0167': '백산',
    '0258': '백양리',
    '0034': '백양사',
    '0089': '벌교',
    '0451': '범일',
    '0198': '별어곡',
    '0069': '보성',
    '0434': '봉성',
    '0175': '봉양',
    '0105': '봉화',
    '0008': '부강',
    '0020': '부산',
    '0190': '부전',
    '0464': '부조',
    '0807': '부천',
    '0222': '북영천',
    '0064': '북천',
    '0166': '분천',
    '0185': '불국사',
    '0636': '비동',
    '0312': '사곡',
    '0255': '사릉',
    '0193': '사방',
    '0121': '사북',
    '0143': '사상',
    '0018': '삼랑진',
    '0044': '삼례',
    '0250': '삼산',
    '0213': '삼탄',
    '0080': '삽교',
    '0272': '상동',
    '0635': '상봉',
    '0156': '상주',
    '0257': '상천',
    '0341': '서경주',
    '0275': '서광주',
    '0025': '서대전',
    '0833': '서빙고',
    '0001': '서울',
    '0243': '서정리',
    '0086': '서천',
    '0325': '석불',
    '0108': '석포',
    '0199': '선평',
    '0248': '성환',
    '0411': '소요산',
    '0142': '소정리',
    '0188': '송정',
    '0551': '수서',
    '0455': '수영',
    '0003': '수원',
    '0051': '순천',
    '0161': '승부',
    '0508': '신경주',
    '0263': '신기',
    '0182': '신녕',
    '0223': '신동',
    '0078': '신례원',
    '0369': '신리',
    '0174': '신림',
    '0416': '신망리',
    '0281': '신창',
    '0465': '신창원',
    '0265': '신탄리',
    '0009': '신탄진',
    '0032': '신태인',
    '0245': '심천',
    '0116': '쌍룡',
    '0503': '아산',
    '0324': '아신',
    '0202': '아우라지',
    '0311': '아포',
    '0192': '안강',
    '0100': '안동',
    '0135': '안양',
    '0230': '약목',
    '0171': '양동',
    '0486': '양보',
    '0269': '양수',
    '0731': '양원',
    '0463': '양자동',
    '0091': '양평',
    '0053': '여수EXPO',
    '0139': '여천',
    '0195': '연당',
    '0220': '연무대',
    '0026': '연산',
    '0415': '연천',
    '0011': '영동',
    '0002': '영등포',
    '0117': '영월',
    '0098': '영주',
    '0103': '영천',
    '0075': '예당',
    '0119': '예미',
    '0079': '예산',
    '0162': '예천',
    '0134': '오근장',
    '0141': '오산',
    '0297': '오송',
    '0047': '오수',
    '0067': '옥곡',
    '0154': '옥산',
    '0892': '옥수',
    '0022': '옥천',
    '0076': '온양온천',
    '0484': '완사',
    '0836': '왕십리',
    '0014': '왜관',
    '0159': '용궁',
    '0347': '용동',
    '0169': '용문',
    '0104': '용산',
    '0919': '운서',
    '0733': '운천',
    '0509': '울산',
    '0084': '웅천',
    '0215': '원동',
    '0479': '원북',
    '0092': '원주',
    '0217': '월내',
    '0383': '율촌',
    '0072': '음성',
    '0101': '의성',
    '0264': '의정부',
    '0055': '이양',
    '0300': '이원',
    '0030': '익산',
    '0921': '인천공항',
    '0227': '일광',
    '0040': '일로',
    '0395': '일산',
    '0204': '일신',
    '0165': '임기',
    '0362': '임성리',
    '0046': '임실',
    '0402': '임진강',
    '0194': '입석리',
    '0212': '입실',
    '0197': '자미원',
    '0446': '장락',
    '0035': '장성',
    '0504': '장항',
    '0414': '전곡',
    '0006': '전의',
    '0045': '전주',
    '0158': '점촌',
    '0262': '정동진',
    '0200': '정선',
    '0033': '정읍',
    '0093': '제천',
    '0088': '조성',
    '0007': '조치원',
    '0126': '좌천',
    '0138': '주덕',
    '0815': '주안',
    '0234': '중리',
    '0071': '증평',
    '0553': '지제',
    '0308': '지탄',
    '0170': '지평',
    '0511': '진례',
    '0066': '진상',
    '0480': '진성',
    '0056': '진영',
    '0063': '진주',
    '0140': '진해',
    '0057': '창원',
    '0512': '창원중앙',
    '0751': '천마산',
    '0005': '천안',
    '0502': '천안아산',
    '0109': '철암',
    '0016': '청도',
    '0090': '청량리',
    '0155': '청리',
    '0253': '청소',
    '0070': '청주',
    '0276': '청주공항',
    '0149': '청평',
    '0412': '초성리',
    '0449': '추전',
    '0133': '추풍령',
    '0106': '춘양',
    '0153': '춘천',
    '0073': '충주',
    '0396': '탄현',
    '0102': '탑리',
    '0714': '태금',
    '0123': '태백',
    '0125': '태화강',
    '0110': '통리',
    '0146': '퇴계원',
    '0400': '파주',
    '0085': '판교',
    '0256': '평내호평',
    '0130': '평촌',
    '0004': '평택',
    '0515': '포항',
    '0097': '풍기',
    '0065': '하동',
    '0238': '하양',
    '0129': '한림정',
    '0413': '한탄강',
    '0196': '함백',
    '0060': '함안',
    '0029': '함열',
    '0157': '함창',
    '0039': '함평',
    '0127': '해운대',
    '0390': '행신',
    '0107': '현동',
    '0211': '호계',
    '0914': '홍대입구',
    '0081': '홍성',
    '0254': '화랑대',
    '0210': '화명',
    '0183': '화본',
    '0054': '화순',
    '0128': '황간',
    '0136': '횡천',
    '0458': '효문',
    '0191': '효자',
    '0274': '효천',
    '0343': '흑석리',
    '0178': '희방사',
}

SEAT_OPTIONS = {
    '015': '일반',
    '021': '휠체어',
    '028': '전동휠체어',
}

SEAT_LOCATIONS = {
    '000': '기본',
    '011': '1인석(특실)',
    '012': '창측',
    '013': '내측',
}
