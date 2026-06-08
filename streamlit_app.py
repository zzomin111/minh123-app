import streamlit as st

st.set_page_config(
    page_title="인수분해 탈출 스트림잇",
    page_icon="🧠",
    layout="centered",
)

st.title("🧮 인수분해 탈출 스트림잇")
st.caption("도입-전개-정리 단계로 구성된 인수분해 탐구형 학습 앱")

st.write(
    "이 앱은 수업의 도입에서 호기심을 자극하고, 전개에서 탐구를 돕고, 정리에서 형성평가를 지원하는 스트림릿 기반 수업 도구입니다."
)

tabs = st.tabs(["1. 도입", "2. 전개", "3. 정리"])

with tabs[0]:
    st.header("1. 도입: 인간 vs AI 계산 대결")
    st.markdown(
        "- 교사가 칠판에 복잡한 수식 문제를 제시합니다.\n"
        "- 학생들은 암산으로 풀어보면서 AI 계산 속도와 풀이 과정을 경험합니다."
    )
    st.markdown(r"**예시 문제:** $7.5^2 \times 3.14 - 2.5^2 \times 3.14$")
    st.write("### 숫자를 입력하고 스트림잇이 계산하는 과정을 확인해 보세요.")

    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("a (첫번째 수)", value=7.5, step=0.5, format="%.2f")
    with col2:
        b = st.number_input("b (두번째 수)", value=2.5, step=0.5, format="%.2f")
    with col3:
        m = st.number_input("m (공통 곱셈 수)", value=3.14, step=0.01, format="%.2f")

    difference = a**2 - b**2
    result = m * difference
    sum_ab = a + b
    diff_ab = a - b
    formula_text = "m(a^2 - b^2) = m(a+b)(a-b)"

    st.markdown("---")
    st.markdown("### AI가 보여주는 공식 적용 과정")
    st.latex(r"%s" % formula_text)
    st.markdown(rf"- 계산할 식: **{m} \times ({a}^2 - {b}^2)**")
    st.markdown(f"- 단계 1: $a+b = {sum_ab}$")
    st.markdown(f"- 단계 2: $a-b = {diff_ab}$")
    st.markdown(rf"- 단계 3: $m(a+b)(a-b) = {m} \times {sum_ab} \times {diff_ab}$")
    st.success(f"정답: {result:.0f}")
    st.info("학생들이 '저걸 저렇게 쉽게 푼다고?' 라고 느끼도록 공식과 계산 과정을 시각적으로 보여줍니다.")

with tabs[1]:
    st.header("2. 전개: 주도적 탐구와 문제 해결")
    st.markdown(
        "- 학생들이 직접 수를 입력하여 인수분해 공식의 구조를 확인합니다.\n"
        "- 교사는 문제를 제시하고 학생들은 스트림잇 앱으로 계산 결과를 검증합니다."
    )
    st.write("### 실제 문제를 입력하여 인수분해 구조를 시각적으로 확인해 보세요.")

    x = st.number_input("왼쪽 수 (예: 103)", value=103, step=1)
    y = st.number_input("오른쪽 수 (예: 97)", value=97, step=1)
    st.markdown("\n---\n")

    if x == y:
        st.warning("두 수가 같으면 일반적인 차의 제곱 공식 대신 제곱 계산이 됩니다. 서로 다른 두 수를 입력하세요.")
    else:
        base = (x + y) / 2
        diff = abs(x - y) / 2
        st.markdown("### 인수분해 구조 분석")
        st.markdown(
            rf"- 입력값: **{x} \times {y}**\n"
            f"- 중심값: **{base}**\n"
            f"- 차이값: **{diff}**\n"
        )

        if base.is_integer() and diff.is_integer():
            base = int(base)
            diff = int(diff)
            st.write("스트림잇은 이 두 수를 중심으로 인수분해 구조를 이렇게 보여줍니다:")
            card1, card2, card3 = st.columns([1, 1, 1])
            card1.metric("(m+d)", f"{base + diff}")
            card2.metric("m^2", f"{base}^2")
            card3.metric("(m-d)", f"{base - diff}")
            st.markdown(
                rf"$\text{{{x}}} \times \text{{{y}}} = (\text{{{base}}}+\text{{{diff}}})(\text{{{base}}}-\text{{{diff}}}) = {base}^2 - {diff}^2$"
            )
            st.success(f"계산 결과: {x * y} = {base**2} - {diff**2} = {base**2 - diff**2}")
        else:
            st.warning(
                "입력한 두 수는 `m + d`, `m - d` 형태로 깔끔하게 나타낼 수 있는 쌍이 아닙니다."
            )
            st.write(f"일반 곱셈 결과: **{x * y}**")

    st.markdown("---")
    st.write("**미션:** 교사가 제시한 문제를 앱에 입력하고, 결과가 차의 제곱 공식과 일치하는지 확인해 보세요.")

with tabs[2]:
    st.header("3. 정리: 형성평가 및 내면화")
    st.markdown(
        "- 실생활 문장제 문제를 풀며 인수분해 공식을 선택하는 능력을 평가합니다.\n"
        "- 정답을 맞히면 재미있는 성공 이펙트를 제공합니다."
    )

    st.write("### 퀴즈: 인수분해 탈출 퀴즈")
    st.markdown(
        r"반지름의 길이가 각각 **55m**, **45m**인 원형 잔디밭의 넓이 차를 구하세요. "
        r"여기에서 $\pi \approx 3.14$를 사용합니다."
    )

    quiz_answer = st.number_input("퀴즈 정답 (숫자로 입력)", value=0.0, format="%.2f")
    quiz_formula = st.radio(
        "사용한 공식 선택",
        (
            "a^2 - b^2 = (a+b)(a-b)",
            "m(a^2 - b^2) = m(a+b)(a-b)",
            "a^2 + b^2 = (a+b)^2 - 2ab",
        ),
    )

    if st.button("정답 확인"):
        correct_value = 1000 * 3.14
        formula_correct = quiz_formula == "m(a^2 - b^2) = m(a+b)(a-b)"
        answer_correct = abs(quiz_answer - correct_value) < 0.5

        if formula_correct and answer_correct:
            st.balloons()
            st.success(
                f"정답입니다! 넓이 차는 약 **{correct_value:.2f}**이고, 사용한 공식은 **{quiz_formula}** 입니다."
            )
            st.write("스트림잇이 제시한 공식을 통해 문제를 빠르고 정확하게 확인할 수 있습니다.")
        elif not formula_correct and answer_correct:
            st.error("답은 맞지만, 선택한 공식이 문제에 가장 적합하지 않습니다. 다시 확인해 보세요.")
        elif formula_correct and not answer_correct:
            st.error("사용한 공식은 맞지만, 계산값이 잘못되었습니다. 다시 계산해 보세요.")
        else:
            st.error("정답과 공식을 다시 확인해 보세요. 필요하면 도입과 전개 탭으로 돌아가 해법을 복습하세요.")

    st.markdown("---")
    st.write("**팁:** 이 퀴즈는 공식 이해와 계산 능력을 동시에 확인하는 형성평가입니다.")
