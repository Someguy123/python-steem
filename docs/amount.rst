Amount
~~~~~~

For the sake of easier handling of Assets on the blockchain

.. code-block:: python

   from steem.amount import Amount
   a = Amount("1 SBD")
   b = Amount("20 SBD")
   a + b
   a * 2
   a += b
   a /= 2.0

.. autoclass:: steem.amount.Amount
   :members:
