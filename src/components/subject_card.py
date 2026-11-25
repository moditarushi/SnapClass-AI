
import streamlit as st
import html
from textwrap import dedent


def subject_card(name, code, section, stats=None,
                 footer_callback=None, subject_id=None):

    name = html.escape(str(name))
    code = html.escape(str(code))
    section = html.escape(str(section))

    card_html = dedent(f"""
    <div style="
        background-color: #ffffff;
        color: #1e293b;
        border: 1px solid #d1d5db;
        border-left: 8px solid #EB459E;
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 20px;
        width: 100%;
        box-sizing: border-box;
    ">
        <h3 style="
            margin: 0;
            color: #1e293b;
            font-size: 1.5rem;
            font-weight: 700;
        ">{name}</h3>

        <p style="color: #475569; margin: 12px 0;">
            Code:
            <span style="
                background-color: #E0E3FF;
                color: #4338CA;
                padding: 4px 9px;
                border-radius: 5px;
                font-weight: 600;
            ">{code}</span>
            | Section: <strong>{section}</strong>
        </p>
    """)

    if stats:
        card_html += """
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
        """

        for icon, label, value in stats:
            card_html += f"""
            <div style="
                background-color: #FCE7F3;
                color: #831843;
                padding: 8px 12px;
                border-radius: 10px;
                font-size: 0.9rem;
            ">
                {icon} <strong>{html.escape(str(value))}</strong>
                {html.escape(str(label))}
            </div>
            """

        card_html += "</div>"

    card_html += "</div>"

    st.html(card_html)

    if footer_callback and st.button(
        "Unenroll from this course",
        key=f"unenroll_{subject_id}",
        type="tertiary",
        width="stretch",
        icon=":material/delete_forever:"
    ):
        footer_callback()
