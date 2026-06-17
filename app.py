import streamlit as st
import random

# 1. 초기 데이터 설정 (게임 저장소)
if 'money' not in st.session_state:
    st.session_state.money = 0
if 'stock_price' not in st.session_state:
    st.session_state.stock_price = 100
if 'owned_stocks' not in st.session_state:
    st.session_state.owned_stocks = 0

st.title("⛏️ 광물 캐기 & 부자 되기 시뮬레이터")

# 왼쪽 사이드바에 내 자산 표시
st.sidebar.header("내 자산")
st.sidebar.write(f"💰 돈: {st.session_state.money}원")
st.sidebar.write(f"📈 보유 주식: {st.session_state.owned_stocks}주")

st.write("---")

# 2. 광물 캐기 (기본 돈벌이)
st.header("1. 광물 캐기")
if st.button("⛏️ 곡괭이질 하기"):
    earned = random.randint(10, 50) # 10~50원 사이 랜덤 수익
    st.session_state.money += earned
    st.success(f"광물을 캐서 {earned}원을 벌었습니다!")

st.write("---")

# 3. 로또 (운 시험)
st.header("2. 인생 역전 로또")
st.write("1장당 100원 (당첨금 1000원, 확률 10%)")
if st.button("🎟️ 로또 구매"):
    if st.session_state.money >= 100:
        st.session_state.money -= 100
        if random.random() < 0.1: # 10% 확률
            st.session_state.money += 1000
            st.balloons() # 당첨 풍선 효과!
            st.success("🎉 당첨!!! 1000원을 얻었습니다!")
        else:
            st.error("꽝! 다음 기회에...")
    else:
        st.warning("돈이 부족합니다!")

st.write("---")

# 4. 주식 시장 (투자)
st.header("3. 주식 시장")
st.write(f"현재 1주당 가격: **{st.session_state.stock_price}원**")

col1, col2, col3 = st.columns(3) # 버튼을 가로로 3개 배치

with col1:
    if st.button("시간 보내기 (주가 변동)"):
        change = random.randint(-30, 30) # 주가가 오르거나 내림
        st.session_state.stock_price += change
        if st.session_state.stock_price < 10: # 최소 가격 방어
            st.session_state.stock_price = 10

with col2:
    if st.button("주식 1주 매수"):
        if st.session_state.money >= st.session_state.stock_price:
            st.session_state.money -= st.session_state.stock_price
            st.session_state.owned_stocks += 1
            st.success("매수 완료!")
        else:
            st.warning("돈이 부족합니다!")

with col3:
    if st.button("주식 1주 매도"):
        if st.session_state.owned_stocks > 0:
            st.session_state.money += st.session_state.stock_price
            st.session_state.owned_stocks -= 1
            st.success("매도 완료!")
        else:
            st.warning("보유한 주식이 없습니다!")
